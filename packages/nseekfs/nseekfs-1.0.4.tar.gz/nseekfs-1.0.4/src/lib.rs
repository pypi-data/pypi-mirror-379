use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use numpy::{PyArray1, PyArray2, PyReadonlyArray2};
use std::sync::Arc;
use std::path::Path;

mod engine;
mod prepare;
mod utils;
use crate::engine::Engine;
use crate::prepare::prepare_bin_from_embeddings;
use crate::utils::vector::SimilarityMetric;

#[pyclass]
#[derive(Debug, Clone)]
pub struct PyQueryItem {
    #[pyo3(get)]
    pub idx: usize,
    #[pyo3(get)]
    pub score: f32,
}

#[pyclass]
#[derive(Debug, Clone)]
pub struct PyQueryResult {
    #[pyo3(get)]
    pub results: Vec<PyQueryItem>,
    #[pyo3(get)]
    pub query_time_ms: f64,
    #[pyo3(get)]
    pub method_used: String,
}

#[pymethods]
impl PyQueryResult {
    fn __repr__(&self) -> String {
        format!(
            "<PyQueryResult results={} time={:.3}ms method={}>",
            self.results.len(),
            self.query_time_ms,
            self.method_used
        )
    }
}

#[pyclass]
pub struct PySearchEngine {
    engine: Arc<Engine>,
}

#[pymethods]
impl PySearchEngine {
    #[new]
    fn new(bin_path: String, ann: bool) -> PyResult<Self> {
        let engine = Engine::new(&bin_path, ann)
            .map_err(|e| PyValueError::new_err(e))?;
        Ok(PySearchEngine { engine: Arc::new(engine) })
    }

    fn dims(&self) -> usize {
        self.engine.dims
    }

    fn rows(&self) -> usize {
        self.engine.rows
    }

    fn query_exact(&self, query: &PyArray1<f32>, k: usize) -> PyResult<PyQueryResult> {
        let slice = unsafe { query.as_slice()? };
        let qr = self.engine.query_exact(slice, k)
            .map_err(|e| PyValueError::new_err(e))?;
        Ok(PyQueryResult {
            results: qr.results.into_iter()
                .map(|(i, s)| PyQueryItem { idx: i, score: s })
                .collect(),
            query_time_ms: qr.query_time_ms,
            method_used: qr.method_used,
        })
    }

    fn query_batch(&self, queries: &PyArray2<f32>, k: usize) -> PyResult<Vec<PyQueryResult>> {
        let slice = unsafe { queries.as_slice()? };
        let dims = queries.shape()[1];
        let all = self.engine.query_batch(slice, dims, k)
            .map_err(|e| PyValueError::new_err(e))?;
        Ok(all.into_iter().map(|qr| PyQueryResult {
            results: qr.results.into_iter()
                .map(|(i, s)| PyQueryItem { idx: i, score: s })
                .collect(),
            query_time_ms: qr.query_time_ms,
            method_used: qr.method_used,
        }).collect())
    }
}

#[pyfunction(signature = (
    embeddings,
    dims,
    rows,
    base_name,
    level,
    normalize = false,
    ann = false,
    seed = 0,
    metric = "cosine",
    output_dir = None,
))]
fn py_prepare_bin_from_embeddings(
    py: Python,
    embeddings: PyReadonlyArray2<f32>,
    dims: usize,
    rows: usize,
    base_name: String,
    level: String,
    normalize: bool,
    ann: bool,
    seed: u64,
    metric: &str,
    output_dir: Option<String>,
) -> PyResult<String> {
    let owned: Vec<f32> = embeddings.as_slice()?.to_vec();
    let metric = SimilarityMetric::from_str(metric)
        .map_err(|e| PyValueError::new_err(e))?;

    let result_path = py.allow_threads(move || {
        prepare_bin_from_embeddings(
            &owned,
            dims,
            rows,
            &base_name,
            &level,
            output_dir.as_ref().map(|s| Path::new(s)),
            ann,
            normalize,
            seed,
            &metric,
        )
    }).map_err(|e| PyValueError::new_err(format!("{:?}", e)))?;

    Ok(result_path.to_string_lossy().to_string())
}

#[pymodule]
fn nseekfs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PySearchEngine>()?;
    m.add_class::<PyQueryResult>()?;
    m.add_function(wrap_pyfunction!(py_prepare_bin_from_embeddings, m)?)?;
    Ok(())
}
