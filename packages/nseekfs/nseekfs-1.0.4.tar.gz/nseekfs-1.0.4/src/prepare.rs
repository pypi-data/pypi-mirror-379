use rayon::prelude::*;
use std::fs::{OpenOptions, remove_file, rename, create_dir_all};
use std::path::{Path, PathBuf};
use wide::f32x8;
use memmap2::MmapMut;
use std::time::Instant;
use dirs;
use log::{info, warn, debug};

#[allow(unused_imports)]
use crate::utils::vector::SimilarityMetric;

const MAX_FILE_SIZE: u64 = 50 * 1024 * 1024 * 1024; // Reduzido para 50GB
const MAX_VECTORS: usize = 50_000_000; // Limite máximo de vetores
const MAX_DIMS: usize = 10_000; // Limite máximo de dimensões

/// Detect SIMD features available (cross-platform safe)
fn detect_simd_features() -> String {
    #[cfg(target_arch = "x86_64")]
    {
        if is_x86_feature_detected!("avx2") {
            return "avx2".to_string();
        } else if is_x86_feature_detected!("avx") {
            return "avx".to_string();
        } else if is_x86_feature_detected!("sse4.2") {
            return "sse4.2".to_string();
        }
    }
    #[cfg(target_arch = "aarch64")]
    {
        return "neon".to_string();
    }
    "scalar".to_string()
}

/// Preparar índice binário com gestão robusta de memória
pub fn prepare_bin_from_embeddings(
    embeddings: &[f32],
    dims: usize,
    rows: usize,
    base_name: &str,
    level: &str,
    output_dir: Option<&std::path::Path>,
    ann: bool,
    normalize: bool,
    _seed: u64,
    metric: &SimilarityMetric,
) -> Result<std::path::PathBuf, String> {
    let total_start = Instant::now();

    // =============== VALIDAÇÕES ROBUSTAS ===============
    validate_inputs(embeddings, dims, rows, base_name, level)?;
    
    // Validar limites de memória
    // Aviso (não bloquear) — podes reativar hard fail com NSEEK_STRICT_MEMCHECK=1
    let estimated_memory = estimate_memory_usage(dims, rows, level)?;
    if let Ok(avail) = get_available_memory() {
        if estimated_memory > avail {
            if std::env::var("NSEEK_STRICT_MEMCHECK").ok().as_deref() == Some("1") {
                return Err(format!(
                    "Insufficient memory: need {:.1}GB, available {:.1}GB",
                    estimated_memory / (1024.0 * 1024.0 * 1024.0),
                    avail / (1024.0 * 1024.0 * 1024.0)
                ));
            } else {
                warn!(
                    "Estimated memory {:.1}MB > available {:.1}MB — a continuar em streaming",
                    estimated_memory / (1024.0 * 1024.0),
                    avail / (1024.0 * 1024.0)
                );
            }
        }
    } else {
        // Sem leitura de RAM → segue em frente (streaming)
        warn!("Could not read available RAM; proceeding with streaming write.");
    }


    info!("✅ Validation passed: {} vectors × {} dims", rows, dims);
    info!("📊 Estimated memory usage: {:.1}MB", estimated_memory / (1024.0 * 1024.0));

    // =============== CONFIGURAÇÃO DE PATHS ===============
    let out_path = resolve_bin_path_safe(output_dir, base_name, level)?;
    create_directory_if_needed(&out_path)?;
    
    let tmp_path = out_path.with_extension("tmp");
    cleanup_temporary_files(&tmp_path, &out_path)?;

    // =============== PROCESSAMENTO STREAMING ===============
    let header_size = 12usize;
    let data_len_f32 = rows * dims;
    let total_size = header_size + data_len_f32 * std::mem::size_of::<f32>();

    info!("🔨 Creating binary file ({:.1}MB)", total_size as f64 / (1024.0 * 1024.0));

    // Criar e configurar ficheiro
    let file = create_and_size_file(&tmp_path, total_size)?;
    let mut mmap = create_memory_map(&file)?;

    // Escrever header
    write_header(&mut mmap, dims, rows, metric)?;

    // Processamento streaming de dados
    let need_norm = should_normalize(metric, normalize);
    process_data_streaming(&mut mmap, embeddings, dims, rows, header_size, need_norm, level)?;

    // Finalizar ficheiro
    finalize_file(mmap, &tmp_path, &out_path)?;

    info!("✅ Binary file created successfully");
    info!("🎯 Total time: {:.2?}", total_start.elapsed());
    
    Ok(out_path)
}

/// Validações completas de entrada
fn validate_inputs(
    embeddings: &[f32],
    dims: usize,
    rows: usize,
    base_name: &str,
    level: &str,
) -> Result<(), String> {
    // Validações básicas
    if dims == 0 || dims > MAX_DIMS {
        return Err(format!("Invalid dims: {} (must be 1-{})", dims, MAX_DIMS));
    }
    if rows == 0 || rows > MAX_VECTORS {
        return Err(format!("Invalid rows: {} (must be 1-{})", rows, MAX_VECTORS));
    }
    if embeddings.len() != dims * rows {
        return Err(format!(
            "Data shape mismatch: expected {}×{}={}, got {}",
            rows, dims, rows * dims, embeddings.len()
        ));
    }
    if base_name.trim().is_empty() || base_name.contains(['/', '\\', '.', ':', '*', '?', '"', '<', '>', '|']) {
        return Err("Invalid base_name: cannot be empty or contain special characters".to_string());
    }
    if !matches!(level, "f32" | "f16" | "f8" | "f64") {
        return Err(format!("Invalid level '{}'. Must be f8, f16, f32, or f64", level));
    }

    // Validação de dados (amostra estatística)
    validate_data_sample(embeddings)?;
    
    Ok(())
}

/// Validar amostra dos dados para detectar problemas
fn validate_data_sample(embeddings: &[f32]) -> Result<(), String> {
    let sample_size = (embeddings.len() / 1000).max(100).min(embeddings.len());
    let step = if sample_size < embeddings.len() {
        embeddings.len() / sample_size
    } else {
        1
    };

    let mut invalid_count = 0;
    let mut zero_count = 0;
    let mut very_large_count = 0;

    for i in (0..embeddings.len()).step_by(step) {
        let val = embeddings[i];
        if !val.is_finite() {
            invalid_count += 1;
        } else if val == 0.0 {
            zero_count += 1;
        } else if val.abs() > 1000.0 {
            very_large_count += 1;
        }
    }

    let sample_count = (embeddings.len() + step - 1) / step;
    if invalid_count > sample_count / 100 {
        return Err(format!(
            "Too many invalid values: {}/{} ({:.1}%)",
            invalid_count, sample_count,
            100.0 * invalid_count as f64 / sample_count as f64
        ));
    }

    if very_large_count > sample_count / 10 {
        warn!("Many large values detected ({} out of {})", very_large_count, sample_count);
    }

    Ok(())
}

/// Estimar uso de memória
fn estimate_memory_usage(dims: usize, rows: usize, level: &str) -> Result<f64, String> {
    let base_size = (dims * rows) as f64 * std::mem::size_of::<f32>() as f64;
    let multiplier = match level {
        "f32" => 1.5,
        "f16" => 2.0,
        "f8"  => 2.5,
        "f64" => 2.0,
        _     => 1.5,
    };
    Ok(base_size * multiplier)
}



/// Obter memória disponível (aproximação)
fn get_available_memory() -> Result<f64, String> {
    #[cfg(target_os = "linux")]
    {
        if let Ok(contents) = std::fs::read_to_string("/proc/meminfo") {
            for line in contents.lines() {
                if line.starts_with("MemAvailable:") {
                    if let Some(kb_str) = line.split_whitespace().nth(1) {
                        if let Ok(kb) = kb_str.parse::<f64>() {
                            return Ok(kb * 1024.0); // Convert to bytes
                        }
                    }
                }
            }
        }
    }
    
    // Fallback conservador
    Ok(8.0 * 1024.0 * 1024.0 * 1024.0) // 8GB
}

/// Criar diretório se necessário
fn create_directory_if_needed(path: &Path) -> Result<(), String> {
    if let Some(parent) = path.parent() {
        if !parent.exists() {
            create_dir_all(parent)
                .map_err(|e| format!("Failed to create directory {}: {}", parent.display(), e))?;
        }
    }
    Ok(())
}

/// Limpar ficheiros temporários
fn cleanup_temporary_files(tmp_path: &Path, out_path: &Path) -> Result<(), String> {
    if tmp_path.exists() {
        remove_file(tmp_path)
            .map_err(|e| format!("Failed to remove temp file: {}", e))?;
    }
    if out_path.exists() {
        remove_file(out_path)
            .map_err(|e| format!("Failed to remove existing file: {}", e))?;
    }
    Ok(())
}

/// Criar e redimensionar ficheiro
fn create_and_size_file(path: &Path, size: usize) -> Result<std::fs::File, String> {
    let file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .truncate(true)
        .open(path)
        .map_err(|e| format!("Failed to create file {}: {}", path.display(), e))?;

    file.set_len(size as u64)
        .map_err(|e| format!("Failed to set file length: {}", e))?;

    Ok(file)
}

/// Criar memory map
fn create_memory_map(file: &std::fs::File) -> Result<MmapMut, String> {
    unsafe {
        MmapMut::map_mut(file)
            .map_err(|e| format!("Failed to create memory map: {}", e))
    }
}

/// Escrever header do ficheiro
fn write_header(
    mmap: &mut MmapMut,
    dims: usize,
    rows: usize,
    metric: &SimilarityMetric,
) -> Result<(), String> {
    let metric_id: u32 = match metric {
        SimilarityMetric::Cosine => 0,
        SimilarityMetric::DotProduct => 1,
        SimilarityMetric::Euclidean => 2,
    };

    mmap[0..4].copy_from_slice(&(dims as u32).to_le_bytes());
    mmap[4..8].copy_from_slice(&(rows as u32).to_le_bytes());
    mmap[8..12].copy_from_slice(&metric_id.to_le_bytes());

    Ok(())
}

/// Determinar se deve normalizar
fn should_normalize(metric: &SimilarityMetric, normalize_flag: bool) -> bool {
    match metric {
        SimilarityMetric::Cosine => true, // Sempre normalizar para cosine
        _ => normalize_flag,
    }
}

/// Processar dados usando streaming para economia de memória
fn process_data_streaming(
    mmap: &mut MmapMut,
    embeddings: &[f32],
    dims: usize,
    rows: usize,
    header_size: usize,
    need_norm: bool,
    level: &str,
) -> Result<(), String> {
    let data_region = &mut mmap[header_size..];
    let out_f32: &mut [f32] = unsafe {
        std::slice::from_raw_parts_mut(
            data_region.as_mut_ptr() as *mut f32,
            rows * dims,
        )
    };

    // Processar em chunks para controlar memória
    let chunk_rows = calculate_chunk_size(rows, dims);
    let mut processed = 0;

    info!("📊 Processing data in chunks of {} rows", chunk_rows);

    while processed < rows {
        let chunk_end = (processed + chunk_rows).min(rows);
        let chunk_size = chunk_end - processed;
        
        let src_start = processed * dims;
        let src_end = chunk_end * dims;
        let dst_start = processed * dims;
        let dst_end = chunk_end * dims;

        let src_chunk = &embeddings[src_start..src_end];
        let dst_chunk = &mut out_f32[dst_start..dst_end];

        if need_norm {
            normalize_chunk_streaming(dst_chunk, src_chunk, dims, chunk_size)?;
        } else {
            dst_chunk.copy_from_slice(src_chunk);
        }

        // Aplicar quantização se necessário
        if level != "f32" {
            warn!("Quantization '{}' not implemented, keeping f32", level);
        }

        processed = chunk_end;
        
        if processed % (chunk_rows * 10) == 0 {
            debug!("Processed {} / {} rows ({:.1}%)", 
                processed, rows, 100.0 * processed as f64 / rows as f64);
        }
    }

    Ok(())
}

/// Calcular tamanho do chunk baseado na memória disponível
fn calculate_chunk_size(rows: usize, dims: usize) -> usize {
    // Tamanho base conservador
    let base_chunk = 8192;
    
    // Ajustar baseado no tamanho dos vetores
    let vector_size_kb = dims * std::mem::size_of::<f32>() / 1024;
    let adjusted_chunk = if vector_size_kb > 4 {
        base_chunk / (vector_size_kb / 4).max(1)
    } else {
        base_chunk
    };

    // Garantir pelo menos 1000 rows por chunk, mas não mais que o total
    adjusted_chunk.max(1000).min(rows)
}

/// Normalizar chunk com processamento streaming
fn normalize_chunk_streaming(
    dst: &mut [f32],
    src: &[f32],
    dims: usize,
    chunk_rows: usize,
) -> Result<(), String> {
    if src.len() != dst.len() || src.len() != chunk_rows * dims {
        return Err("Chunk size mismatch in normalization".to_string());
    }

    dst.par_chunks_mut(dims)
        .zip(src.par_chunks(dims))
        .enumerate()
        .try_for_each(|(row_idx, (dst_row, src_row))| -> Result<(), String> {
            // Calcular norma com SIMD quando possível
            let mut sum = 0.0f32;
            
            if dims >= 8 {
                let chunks_8 = dims / 8;
                for i in 0..chunks_8 {
                    let start = i * 8;
                    let values = [
                        src_row[start], src_row[start+1], src_row[start+2], src_row[start+3],
                        src_row[start+4], src_row[start+5], src_row[start+6], src_row[start+7],
                    ];
                    let simd = f32x8::from(values);
                    sum += (simd * simd).reduce_add();
                }
                
                // Processar resto
                for &val in &src_row[chunks_8 * 8..] {
                    sum += val * val;
                }
            } else {
                for &val in src_row {
                    sum += val * val;
                }
            }

            let norm = sum.sqrt();
            
            if norm == 0.0 || !norm.is_finite() {
                // Vetor inválido - preencher com zeros
                for val in dst_row.iter_mut() {
                    *val = 0.0;
                }
                warn!("Invalid vector at row {} (norm: {})", row_idx, norm);
            } else if norm < 1e-10 {
                // Norma muito pequena - normalizar mas avisar
                let inv_norm = 1.0 / norm;
                for (dst_val, &src_val) in dst_row.iter_mut().zip(src_row.iter()) {
                    *dst_val = src_val * inv_norm;
                }
                warn!("Very small norm at row {}: {}", row_idx, norm);
            } else {
                // Normalização normal
                let inv_norm = 1.0 / norm;
                for (dst_val, &src_val) in dst_row.iter_mut().zip(src_row.iter()) {
                    *dst_val = src_val * inv_norm;
                }
            }
            
            Ok(())
        })?;

    Ok(())
}

/// Finalizar ficheiro com verificações
fn finalize_file(
    mmap: MmapMut,
    tmp_path: &Path,
    final_path: &Path,
) -> Result<(), String> {
    // Flush e verificar
    mmap.flush()
        .map_err(|e| format!("Failed to flush memory map: {}", e))?;
    
    drop(mmap); // Fechar mmap antes de mover o ficheiro

    // Verificar tamanho do ficheiro
    let actual_size = std::fs::metadata(tmp_path)
        .map_err(|e| format!("Failed to get temp file metadata: {}", e))?
        .len();

    // Mover ficheiro temporário para local final
    rename(tmp_path, final_path)
        .map_err(|e| format!("Failed to move temp file to final location: {}", e))?;

    info!("📁 File finalized: {} ({:.2}MB)", 
        final_path.display(), 
        actual_size as f64 / (1024.0 * 1024.0)
    );

    Ok(())
}

/// Resolver path do ficheiro binário de forma segura
pub fn resolve_bin_path_safe(
    output_dir: Option<&Path>,
    base_name: &str,
    level: &str,
) -> Result<PathBuf, String> {
    // Validar base_name
    if base_name.trim().is_empty() {
        return Err("Base name cannot be empty".to_string());
    }
    if base_name.contains(['/', '\\', ':', '*', '?', '"', '<', '>', '|', '.']) {
        return Err("Base name contains invalid characters".to_string());
    }

    let sanitized_name = base_name.chars()
        .filter(|c| c.is_alphanumeric() || *c == '_' || *c == '-')
        .collect::<String>();
    
    if sanitized_name.is_empty() {
        return Err("Base name contains no valid characters".to_string());
    }

    let final_path: PathBuf = match output_dir {
        Some(dir) => {
            if !dir.exists() {
                debug!("Output directory doesn't exist, will create: {:?}", dir);
            } else if !dir.is_dir() {
                return Err(format!("Output path is not a directory: {:?}", dir));
            }
            dir.join(format!("{}_{}.bin", sanitized_name, level))
        }
        None => {
            let home = dirs::home_dir()
                .ok_or("Failed to get home directory")?;
            let nseek_dir = home.join(".nseek").join("indexes");
            nseek_dir.join(format!("{}_{}.bin", sanitized_name, level))
        }
    };

    Ok(final_path)
}

#[cfg(test)]
mod tests {
    use super::*;
    use tempfile::tempdir;

    #[test]
    fn test_input_validation() {
        // Test valid inputs
        let embeddings = vec![1.0f32; 1000];
        assert!(validate_inputs(&embeddings, 10, 100, "test", "f32").is_ok());

        // Test invalid dimensions
        assert!(validate_inputs(&embeddings, 0, 100, "test", "f32").is_err());
        assert!(validate_inputs(&embeddings, MAX_DIMS + 1, 100, "test", "f32").is_err());

        // Test invalid base name
        assert!(validate_inputs(&embeddings, 10, 100, "", "f32").is_err());
        assert!(validate_inputs(&embeddings, 10, 100, "test/bad", "f32").is_err());

        // Test shape mismatch
        assert!(validate_inputs(&embeddings, 10, 200, "test", "f32").is_err());
    }

    #[test]
    fn test_memory_estimation() {
        let mem = estimate_memory_usage(100, 1000, "f32").unwrap();
        assert!(mem > 0.0);
        
        let mem_f16 = estimate_memory_usage(100, 1000, "f16").unwrap();
        assert!(mem_f16 > mem); // f16 should use more memory during processing
    }

    #[test]
    fn test_chunk_size_calculation() {
        let chunk = calculate_chunk_size(100_000, 384);
        assert!(chunk > 0);
        assert!(chunk <= 100_000);
        
        // Large dimensions should result in smaller chunks
        let chunk_large = calculate_chunk_size(100_000, 2048);
        assert!(chunk_large <= chunk);
    }

    #[test]
    fn test_path_resolution() {
        let temp_dir = tempdir().unwrap();
        
        // Test with output directory
        let path = resolve_bin_path_safe(Some(temp_dir.path()), "test", "f32").unwrap();
        assert!(path.to_string_lossy().contains("test_f32.bin"));
        
        // Test with invalid characters
        let result = resolve_bin_path_safe(Some(temp_dir.path()), "test/bad", "f32");
        assert!(result.is_err());
        
        // Test with empty name
        let result = resolve_bin_path_safe(Some(temp_dir.path()), "", "f32");
        assert!(result.is_err());
    }

    #[test]
    fn test_data_validation() {
        // Valid data
        let good_data = vec![1.0, 2.0, 3.0, 4.0];
        assert!(validate_data_sample(&good_data).is_ok());
        
        // Data with some NaN values (should fail if too many)
        let mut bad_data = vec![1.0; 1000];
        for i in (0..100).step_by(10) {
            bad_data[i] = f32::NAN;
        }
        assert!(validate_data_sample(&bad_data).is_err());
        
        // Data with large values (should warn but not fail)
        let large_data = vec![1000.0; 100];
        assert!(validate_data_sample(&large_data).is_ok());
    }

    #[test]
    fn test_normalize_chunk() {
        let dims = 4;
        let rows = 2;
        let src = vec![3.0, 4.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0];
        let mut dst = vec![0.0; 8];
        
        normalize_chunk_streaming(&mut dst, &src, dims, rows).unwrap();
        
        // First vector: [3,4,0,0] -> norm = 5 -> [0.6, 0.8, 0, 0]
        assert!((dst[0] - 0.6).abs() < 1e-6);
        assert!((dst[1] - 0.8).abs() < 1e-6);
        assert!((dst[2] - 0.0).abs() < 1e-6);
        assert!((dst[3] - 0.0).abs() < 1e-6);
        
        // Second vector: [1,1,1,1] -> norm = 2 -> [0.5, 0.5, 0.5, 0.5]
        for i in 4..8 {
            assert!((dst[i] - 0.5).abs() < 1e-6);
        }
    }

    #[test]
    fn test_streaming_preparation() {
        let temp_dir = tempdir().unwrap();
        
        // Create test data
        let dims = 10;
        let rows = 100;
        let embeddings: Vec<f32> = (0..dims * rows).map(|i| i as f32 / 1000.0).collect();
        
        let result = prepare_bin_from_embeddings(
            &embeddings,
            dims,
            rows,
            "test_streaming",
            "f32",
            Some(temp_dir.path()),
            false, // no ANN
            true,  // normalize
            0,     // seed
            &SimilarityMetric::Cosine,
        );
        
        assert!(result.is_ok());
        let path = result.unwrap();
        assert!(path.exists());
        
        // Verify file size
        let file_size = std::fs::metadata(&path).unwrap().len();
        let expected_size = 12 + (dims * rows * 4); // header + data
        assert_eq!(file_size, expected_size as u64);
    }

    #[test]
    fn test_memory_limits() {
        // Test with unrealistic large data that should fail memory check
        let dims = 10000;
        let rows = 1000000;
        let embeddings = vec![1.0f32; 100]; // Much smaller than claimed
        
        let result = prepare_bin_from_embeddings(
            &embeddings,
            dims,
            rows,
            "test_large",
            "f32",
            None,
            false,
            false,
            0,
            &SimilarityMetric::Cosine,
        );
        
        // Should fail due to shape mismatch or memory limits
        assert!(result.is_err());
    }
}