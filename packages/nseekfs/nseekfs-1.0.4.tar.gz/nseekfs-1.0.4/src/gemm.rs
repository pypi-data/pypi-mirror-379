#[cfg(feature = "blas")]
use cblas_sys::{
    cblas_sgemm,
    CBLAS_ORDER::CblasRowMajor,
    CBLAS_TRANSPOSE::{CblasNoTrans, CblasTrans},
};

/// produto C = A(m×k) * B^T(n×k), tudo row-major
/// A: lda=k, B: ldb=k, C: ldc=n
pub fn sgemm_rowmajor_atbt(
    m: usize, n: usize, k: usize,
    a: *const f32, lda: usize,
    b: *const f32, ldb: usize,
    c: *mut f32, ldc: usize,
) {
    #[cfg(feature = "blas")]
    unsafe {
        cblas_sgemm(
            CblasRowMajor,
            CblasNoTrans, // A
            CblasTrans,   // B^T
            m as i32, n as i32, k as i32,
            1.0f32,
            a, lda as i32,
            b, ldb as i32,
            0.0f32,
            c, ldc as i32,
        );
        return;
    }

    // fallback puro-Rust (single-thread) — estável e portátil
    unsafe {
        matrixmultiply::sgemm(
            m, n, k,
            1.0f32,
            a, k as isize, 1,      // A row-major
            b, 1, k as isize,      // B^T
            0.0f32,
            c, n as isize, 1,      // C row-major
        );
    }
}
