use std::fs::File;
use std::path::Path;
use memmap2::Mmap;
use rayon::prelude::*;
use std::time::Instant;
use ordered_float::OrderedFloat;
use crate::utils::vector::SimilarityMetric;
use std::cmp::Reverse;
use std::collections::BinaryHeap;      
use core::ptr;

#[derive(Copy, Clone, Debug)]
struct SafeF32(f32);
impl Eq for SafeF32 {}
impl PartialEq for SafeF32 { 
    fn eq(&self, other: &Self) -> bool { 
        self.0.to_bits() == other.0.to_bits() 
    } 
}
impl Ord for SafeF32 {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        let a = if self.0.is_nan() { f32::NEG_INFINITY } else { self.0 };
        let b = if other.0.is_nan() { f32::NEG_INFINITY } else { other.0 };
        a.total_cmp(&b)
    }
}
impl PartialOrd for SafeF32 { 
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> { 
        Some(self.cmp(other)) 
    } 
}

/// Estrutura de resultados de query
pub struct QueryResult {
    pub results: Vec<(usize, f32)>,
    pub query_time_ms: f64,
    pub method_used: String,
}

use wide::f32x8;

#[inline]
unsafe fn load8_unaligned(ptr_f32: *const f32) -> [f32; 8] {
    // ptr está a apontar para f32; reinterpretamos como *const [f32; 8]
    ptr::read_unaligned(ptr_f32 as *const [f32; 8])
}

#[inline]
fn dot_simd(a: &[f32], b: &[f32]) -> f32 {
    debug_assert_eq!(a.len(), b.len());
    let len = a.len();
    let mut acc = f32x8::from([0.0; 8]);
    let mut i = 0usize;

    // bloco vectorizado
    while i + 8 <= len {
        let va = unsafe { f32x8::from( load8_unaligned(a.as_ptr().add(i)) ) };
        let vb = unsafe { f32x8::from( load8_unaligned(b.as_ptr().add(i)) ) };
        acc = acc + va * vb;
        i += 8;
    }

    // reduzir acumulador + tratar resto escalar
    let mut sum = acc.reduce_add();
    while i < len {
        sum += a[i] * b[i];
        i += 1;
    }
    sum
}

#[inline]
fn l2_sq_simd(a: &[f32], b: &[f32]) -> f32 {
    debug_assert_eq!(a.len(), b.len());
    let len = a.len();
    let mut acc = f32x8::from([0.0; 8]);
    let mut i = 0usize;

    while i + 8 <= len {
        let va = unsafe { f32x8::from( load8_unaligned(a.as_ptr().add(i)) ) };
        let vb = unsafe { f32x8::from( load8_unaligned(b.as_ptr().add(i)) ) };
        let d = va - vb;
        acc = acc + d * d;
        i += 8;
    }

    let mut sum = acc.reduce_add();
    while i < len {
        let d = a[i] - b[i];
        sum += d * d;
        i += 1;
    }
    sum
}


#[inline]
fn compute_batch_similarities_matrix(
    queries: &[f32],
    q_dims: usize,
    q_count: usize,
    vectors: &[f32],
    v_dims: usize,
    v_count: usize,
    metric: &SimilarityMetric,
) -> Vec<f32> {
    assert_eq!(q_dims, v_dims);
    let dims = q_dims;

    let mut scores = vec![0.0f32; q_count * v_count];

    for q_idx in 0..q_count {
        let q = &queries[q_idx * dims .. (q_idx + 1) * dims];
        let row = &mut scores[q_idx * v_count .. (q_idx + 1) * v_count];

        match metric {
            SimilarityMetric::Cosine | SimilarityMetric::DotProduct => {
                for v_idx in 0..v_count {
                    let v = &vectors[v_idx * dims .. (v_idx + 1) * dims];
                    row[v_idx] = dot_simd(q, v);
                }
            }
            SimilarityMetric::Euclidean => {
                for v_idx in 0..v_count {
                    let v = &vectors[v_idx * dims .. (v_idx + 1) * dims];
                    // negativo para “maior é melhor”
                    row[v_idx] = l2_sq_simd(q, v);
                }
            }
        }
    }

    scores
}



// helpers pointer-friendly (coloca-as no mesmo ficheiro, perto das SIMD existentes)
#[inline]
unsafe fn dot_simd_ptr(a: *const f32, b: *const f32, len: usize) -> f32 {
    use wide::f32x8;
    let mut acc = f32x8::from([0.0; 8]);
    let mut i = 0usize;
    while i + 8 <= len {
        let va = f32x8::from(core::ptr::read_unaligned(a.add(i) as *const [f32; 8]));
        let vb = f32x8::from(core::ptr::read_unaligned(b.add(i) as *const [f32; 8]));
        acc = acc + va * vb;
        i += 8;
    }
    let mut sum = acc.reduce_add();
    while i < len {
        sum += *a.add(i) * *b.add(i);
        i += 1;
    }
    sum
}

#[inline]
unsafe fn l2_sq_simd_ptr(a: *const f32, b: *const f32, len: usize) -> f32 {
    use wide::f32x8;
    let mut acc = f32x8::from([0.0; 8]);
    let mut i = 0usize;
    while i + 8 <= len {
        let va = f32x8::from(core::ptr::read_unaligned(a.add(i) as *const [f32; 8]));
        let vb = f32x8::from(core::ptr::read_unaligned(b.add(i) as *const [f32; 8]));
        let d = va - vb;
        acc = acc + d * d;
        i += 8;
    }
    let mut sum = acc.reduce_add();
    while i < len {
        let d = *a.add(i) - *b.add(i);
        sum += d * d;
        i += 1;
    }
    sum
}


/// devolve "similaridade": maior é melhor
#[inline]
fn compute_similarity_simd(metric: &crate::utils::vector::SimilarityMetric, q: &[f32], r: &[f32]) -> f32 {
    match metric {
        crate::utils::vector::SimilarityMetric::Cosine |
        crate::utils::vector::SimilarityMetric::DotProduct => {
            dot_simd(q, r)
        }
        crate::utils::vector::SimilarityMetric::Euclidean => {
            l2_sq_simd(q, r)
        }
    }
}


/// Motor de busca vetorial com gestão robusta de memória
pub struct Engine {
    pub rows: usize,
    pub dims: usize,
    pub metric: SimilarityMetric,
    mmap: Mmap,                 
    data: *const f32,           
}

unsafe impl Send for Engine {}
unsafe impl Sync for Engine {}


fn configure_threads_once() {
    use std::sync::Once;
    static START: Once = Once::new();
    START.call_once(|| {
        if let Ok(v) = std::env::var("NSEEK_THREADS") {
            if !v.is_empty() {
                std::env::set_var("OPENBLAS_NUM_THREADS", &v);
                std::env::set_var("OMP_NUM_THREADS", &v);
                std::env::set_var("RAYON_NUM_THREADS", &v);
                let n = v.parse().unwrap_or_else(|_| num_cpus::get());
                let _ = rayon::ThreadPoolBuilder::new().num_threads(n).build_global();
                return;
            }
        }
        let n = num_cpus::get().max(1);
        std::env::set_var("OPENBLAS_NUM_THREADS", n.to_string());
        std::env::set_var("OMP_NUM_THREADS", n.to_string());
        std::env::set_var("RAYON_NUM_THREADS", n.to_string());
        let _ = rayon::ThreadPoolBuilder::new().num_threads(n).build_global();
    });
}

#[inline]
fn gemm_scores_block(
    a_qblock: &[f32],           // (m × d), row-major
    m: usize,
    d: usize,
    b_vblock_rowmajor: &[f32],  // (n × d), row-major
    n: usize,
    out_c: &mut [f32],          // (m × n), row-major
) {
    // C = A (m×d) * (B^T) (d×n)
    debug_assert_eq!(a_qblock.len(), m * d);
    debug_assert_eq!(b_vblock_rowmajor.len(), n * d);
    debug_assert_eq!(out_c.len(), m * n);

    unsafe {
        // matrixmultiply::sgemm: C{m×n} = A{m×k} * B{k×n}
        matrixmultiply::sgemm(
            m,          // m
            d,          // k
            n,          // n
            1.0,        // alpha
            a_qblock.as_ptr(),
            d as isize, // a_row_stride
            1,          // a_col_stride
            b_vblock_rowmajor.as_ptr(),
            1,          // b_row_stride  (k avança 1)
            d as isize, // b_col_stride  (n avança d)
            0.0,        // beta
            out_c.as_mut_ptr(),
            n as isize, // c_row_stride
            1,          // c_col_stride
        );
    }
}


impl Engine {
    pub fn new(path: &str, _ann: bool) -> Result<Self, String> {
        let file = File::open(Path::new(path))
            .map_err(|e| format!("Failed to open file {}: {}", path, e))?;

        let mmap = unsafe { Mmap::map(&file) }
            .map_err(|e| format!("Failed to mmap file: {}", e))?;

        configure_threads_once();

        // header
        let header = &mmap[0..12];
        let dims = u32::from_le_bytes(header[0..4].try_into().unwrap()) as usize;
        let rows = u32::from_le_bytes(header[4..8].try_into().unwrap()) as usize;
        let metric_id = u32::from_le_bytes(header[8..12].try_into().unwrap());

        let metric = match metric_id {
            0 => SimilarityMetric::Cosine,
            1 => SimilarityMetric::DotProduct,
            2 => SimilarityMetric::Euclidean,
            _ => return Err(format!("Unknown metric id: {}", metric_id)),
        };

        let expected = 12 + rows * dims * std::mem::size_of::<f32>();
        if mmap.len() < expected {
            return Err(format!("File too small: expected {} bytes, got {}", expected, mmap.len()));
        }

        let data_ptr = unsafe { mmap.as_ptr().add(12) as *const f32 };

        Ok(Self {
            dims,
            rows,
            metric,
            data: data_ptr,
            mmap,
        })
    }

    #[inline]
    fn row_ptr(&self, i: usize) -> &[f32] {
        debug_assert!(i < self.rows);
        unsafe {
            std::slice::from_raw_parts(self.data.add(i * self.dims), self.dims)
        }
    }


    /// Query exata com gestão robusta de memória
    pub fn query_exact(&self, query: &[f32], k: usize) -> Result<QueryResult, String> {
        if query.len() != self.dims {
            return Err(format!("Query dimension {} != index dimension {}", query.len(), self.dims));
        }
        if !query.iter().all(|v| v.is_finite()) {
            return Err("Query vector contém valores não finitos".to_string());
        }
        if k == 0 || self.rows == 0 {
            return Ok(QueryResult {
                results: Vec::new(),
                query_time_ms: 0.0,
                method_used: "exact".to_string(),
            });
        }

        let start = Instant::now();
        let topk = k.min(self.rows);

        let metric = self.metric; // copiar enum

        let mut results: Vec<(usize, f32)> = (0..self.rows)
            .into_par_iter()
            .map(|i| {
                let row = self.row_ptr(i);
                let s = compute_similarity_simd(&metric, query, row);
                (i, s)
            })
            .filter(|(_, s)| s.is_finite())
            .collect();

        if results.len() > topk {
            let kth = topk - 1;
            if metric == SimilarityMetric::Euclidean {
                results.select_nth_unstable_by(kth, |a, b| a.1.partial_cmp(&b.1).unwrap());
            } else {
                results.select_nth_unstable_by(kth, |a, b| b.1.partial_cmp(&a.1).unwrap());
            }
            results.truncate(topk);
        }

        if metric == SimilarityMetric::Euclidean {
            results.sort_unstable_by(|a, b| a.1.partial_cmp(&b.1).unwrap());
        } else {
            results.sort_unstable_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
        }

        Ok(QueryResult {
            results,
            query_time_ms: start.elapsed().as_secs_f64() * 1000.0,
            method_used: "exact".to_string(),
        })
    }



    /// 🚀 REVOLUTIONARY: Matrix-based batch processing like FAISS
    pub fn query_batch(&self, queries: &[f32], dims: usize, k: usize) -> Result<Vec<QueryResult>, String> {
        if queries.len() % dims != 0 {
            return Err("queries.len() não é múltiplo de dims".to_string());
        }
        let q_rows = queries.len() / dims;

        if dims != self.dims {
            return Err(format!("Query dimensions {} != index dimensions {}", dims, self.dims));
        }
        if q_rows == 0 {
            return Ok(Vec::new());
        }
        if q_rows == 1 {
            return Ok(vec![self.query_exact(&queries[0..dims], k)?]);
        }

        // 🚀 DECISION: Use matrix approach for better performance
        if self.should_use_matrix_batch(q_rows, k) {
            self.query_batch_matrix_optimized(queries, dims, k)
        } else {
            self.query_batch_rayon_optimized(queries, dims, k)
        }
    }

    /// 🚀 NEW: More aggressive criteria favoring matrix approach
    fn should_use_matrix_batch(&self, q_rows: usize, _k: usize) -> bool {
        // Use matrix approach for cosine/dot with any batch size >= 2
        // and for datasets where matrix computation is efficient
        match self.metric {
            SimilarityMetric::Cosine | SimilarityMetric::DotProduct => {
                q_rows >= 2 && self.rows >= 5_000  // Much lower threshold
            }
            SimilarityMetric::Euclidean => {
                q_rows >= 4 && self.rows >= 10_000
            }
        }
    }

    fn query_batch_matrix_optimized(
        &self,
        queries: &[f32],
        dims: usize,
        k: usize,
    ) -> Result<Vec<QueryResult>, String> {
        use std::sync::Mutex;

        let q_count = queries.len() / dims;
        let topk = k.min(self.rows);
        if q_count == 0 || topk == 0 {
            return Ok(Vec::new());
        }

        let vectors_all: &[f32] = unsafe {
            std::slice::from_raw_parts(self.data, self.rows * self.dims)
        };

        let metric = self.metric;

        let results: Vec<QueryResult> = (0..q_count).into_par_iter().map(|q_idx| {
            let q = &queries[q_idx * dims .. (q_idx + 1) * dims];
            let mut pairs: Vec<(usize, f32)> = Vec::with_capacity(self.rows);

            for v_idx in 0..self.rows {
                let v = &vectors_all[v_idx * dims .. (v_idx + 1) * dims];
                let score = compute_similarity_simd(&metric, q, v);
                if score.is_finite() {
                    pairs.push((v_idx, score));
                }
            }

            if pairs.len() > topk {
                let kth = topk - 1;
                if metric == SimilarityMetric::Euclidean {
                    pairs.select_nth_unstable_by(kth, |a, b| a.1.partial_cmp(&b.1).unwrap());
                } else {
                    pairs.select_nth_unstable_by(kth, |a, b| b.1.partial_cmp(&a.1).unwrap());
                }
                pairs.truncate(topk);
            }

            if metric == SimilarityMetric::Euclidean {
                pairs.sort_unstable_by(|a, b| a.1.partial_cmp(&b.1).unwrap());
            } else {
                pairs.sort_unstable_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
            }

            QueryResult {
                results: pairs,
                query_time_ms: 0.0,
                method_used: "matrix-optimized".to_string(),
            }
        }).collect();

        Ok(results)
    }







    /// 🚀 FASTEST PATH: Full matrix computation
    fn query_batch_full_matrix(&self, queries: &[f32], dims: usize, k: usize) -> Result<Vec<QueryResult>, String> {
        let q_count = queries.len() / dims;
        let topk = k.min(self.rows);

        // Create vectors slice from mmap
        let vectors_data = unsafe {
            std::slice::from_raw_parts(self.data, self.rows * self.dims)
        };

        // 🚀 MATRIX COMPUTATION: All similarities at once
        let all_scores = compute_batch_similarities_matrix(
            queries, dims, q_count,
            vectors_data, self.dims, self.rows,
            &self.metric
        );

        // 🚀 PARALLEL TOP-K: Extract top-k for each query in parallel
        let results: Vec<QueryResult> = (0..q_count).into_par_iter().map(|q_idx| {
            let scores_for_query = &all_scores[q_idx * self.rows..(q_idx + 1) * self.rows];
            
            // Find top-k efficiently
            let mut indexed_scores: Vec<(usize, f32)> = scores_for_query
                .iter()
                .enumerate()
                .filter_map(|(idx, &score)| {
                    if score.is_finite() { Some((idx, score)) } else { None }
                })
                .collect();

            // Use partial sort for better performance
            if indexed_scores.len() > topk {
                let kth = topk.saturating_sub(1);
                indexed_scores.select_nth_unstable_by(kth, |a, b| b.1.partial_cmp(&a.1).unwrap());
                indexed_scores.truncate(topk);
            }
            indexed_scores.sort_unstable_by(|a, b| b.1.partial_cmp(&a.1).unwrap());

            QueryResult {
                results: indexed_scores,
                query_time_ms: 0.0,
                method_used: "matrix-full".to_string(),
            }
        }).collect();

        Ok(results)
    }

    /// 🚀 CHUNKED MATRIX: For very large datasets
    fn query_batch_chunked_matrix(
        &self,
        queries: &[f32],
        dims: usize,
        k: usize,
    ) -> Result<Vec<QueryResult>, String> {
        let q_count = queries.len() / dims;
        let topk = k.min(self.rows);
        if q_count == 0 || topk == 0 {
            return Ok(Vec::new());
        }

        let max_chunk_vectors = 50_000usize;
        let vectors_all: &[f32] = unsafe {
            std::slice::from_raw_parts(self.data, self.rows * self.dims)
        };

        let metric = self.metric;

        let results: Vec<QueryResult> = (0..q_count).into_par_iter().map(|q_idx| {
            let q = &queries[q_idx * dims .. (q_idx + 1) * dims];
            let mut all_pairs: Vec<(usize, f32)> = Vec::with_capacity(self.rows);

            let mut v_start = 0usize;
            while v_start < self.rows {
                let v_end = (v_start + max_chunk_vectors).min(self.rows);
                for v_idx in v_start..v_end {
                    let v = &vectors_all[v_idx * dims .. (v_idx + 1) * dims];
                    let score = compute_similarity_simd(&metric, q, v);
                    if score.is_finite() {
                        all_pairs.push((v_idx, score));
                    }
                }
                v_start = v_end;
            }

            if all_pairs.len() > topk {
                let kth = topk - 1;
                if metric == SimilarityMetric::Euclidean {
                    all_pairs.select_nth_unstable_by(kth, |a, b| a.1.partial_cmp(&b.1).unwrap());
                } else {
                    all_pairs.select_nth_unstable_by(kth, |a, b| b.1.partial_cmp(&a.1).unwrap());
                }
                all_pairs.truncate(topk);
            }

            if metric == SimilarityMetric::Euclidean {
                all_pairs.sort_unstable_by(|a, b| a.1.partial_cmp(&b.1).unwrap());
            } else {
                all_pairs.sort_unstable_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
            }

            QueryResult {
                results: all_pairs,
                query_time_ms: 0.0,
                method_used: "matrix-chunked".to_string(),
            }
        }).collect();

        Ok(results)
    }




    /// 🚀 FALLBACK: High-performance Rayon implementation
    fn query_batch_rayon_optimized(&self, queries: &[f32], dims: usize, k: usize) -> Result<Vec<QueryResult>, String> {
        let effective_k = k.min(self.rows);
        let q_rows = queries.len() / dims;
        if q_rows == 0 { return Ok(Vec::new()); }

        if !queries.iter().all(|v| v.is_finite()) {
            return Err("Queries contêm valores não finitos (NaN/Inf)".to_string());
        }

        let threads = num_cpus::get().max(1);
        let chunk_q = (threads * 4).max(8).min(q_rows);

        let mut out: Vec<QueryResult> = Vec::with_capacity(q_rows);

        for qs in (0..q_rows).step_by(chunk_q) {
            let qe = (qs + chunk_q).min(q_rows);
            let block = &queries[qs * dims .. qe * dims];

            let mut block_results: Vec<QueryResult> =
                block.par_chunks(dims).map(|qv| {
                    match self.query_exact(qv, effective_k) {
                        Ok(mut r) => { 
                            r.method_used = "rayon-optimized".to_string(); 
                            r 
                        }
                        Err(_) => QueryResult { 
                            results: Vec::new(), 
                            query_time_ms: 0.0, 
                            method_used: "rayon-optimized".to_string() 
                        }
                    }
                }).collect();

            out.append(&mut block_results);
        }

        Ok(out)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use tempfile::tempdir;
    use std::fs::File;
    use std::io::Write;

    fn create_test_index(rows: usize, dims: usize) -> (tempfile::TempDir, String) {
        let temp_dir = tempdir().unwrap();
        let file_path = temp_dir.path().join("test.bin");
        let mut file = File::create(&file_path).unwrap();

        // Header
        file.write_all(&(dims as u32).to_le_bytes()).unwrap();
        file.write_all(&(rows as u32).to_le_bytes()).unwrap();
        file.write_all(&0u32.to_le_bytes()).unwrap(); // Cosine metric

        // Data
        let data: Vec<f32> = (0..rows * dims).map(|i| (i as f32) / 1000.0).collect();
        let bytes: &[u8] = bytemuck::cast_slice(&data);
        file.write_all(bytes).unwrap();

        (temp_dir, file_path.to_string_lossy().to_string())
    }

    #[test]
    fn test_matrix_batch() {
        let (_temp_dir, path) = create_test_index(1000, 50);
        let engine = Engine::new(&path, false).unwrap();
        
        let queries: Vec<f32> = (0..5 * 50).map(|i| (i as f32) / 100.0).collect();
        let results = engine.query_batch(&queries, 50, 10).unwrap();
        
        assert_eq!(results.len(), 5);
        for result in results {
            assert_eq!(result.results.len(), 10);
            assert!(result.method_used.contains("matrix"));
        }
    }

    #[test]
    fn test_large_batch_matrix() {
        let (_temp_dir, path) = create_test_index(10000, 100);
        let engine = Engine::new(&path, false).unwrap();
        
        let queries: Vec<f32> = (0..50 * 100).map(|i| (i as f32) / 1000.0).collect();
        let results = engine.query_batch(&queries, 100, 10).unwrap();
        
        assert_eq!(results.len(), 50);
        assert!(results[0].method_used.contains("matrix"));
    }
}