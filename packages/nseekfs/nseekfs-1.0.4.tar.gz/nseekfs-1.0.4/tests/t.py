#!/usr/bin/env python3
"""
Benchmark comparativo: NSeekFS vs NumPy vs FAISS
Mede build, query unitária e batch de queries
em múltiplos cenários.
"""

import time
import numpy as np

try:
    import faiss
except ImportError:
    faiss = None
    print("⚠️ FAISS não está instalado (pip install faiss-cpu)")

import nseekfs


# ========= Gerador de dados =========
def generate_embeddings(n=10000, dims=128, seed=42, normalize=False):
    rng = np.random.default_rng(seed)
    X = rng.normal(0, 1, size=(n, dims)).astype(np.float32)
    if normalize:
        X /= np.linalg.norm(X, axis=1, keepdims=True) + 1e-9
    return X


# ========= NumPy =========
def numpy_search(X, q, metric, top_k):
    if metric == "cosine":
        sims = X @ q / (np.linalg.norm(X, axis=1) * np.linalg.norm(q) + 1e-9)
        idx = np.argsort(-sims)[:top_k]
        return [{"idx": int(i), "score": float(sims[i])} for i in idx]
    elif metric == "dot":
        sims = X @ q
        idx = np.argsort(-sims)[:top_k]
        return [{"idx": int(i), "score": float(sims[i])} for i in idx]
    elif metric == "euclidean":
        # L2² para alinhar com FAISS
        dists = np.sum((X - q) ** 2, axis=1)
        idx = np.argsort(dists)[:top_k]
        return [{"idx": int(i), "score": float(dists[i])} for i in idx]
    else:
        raise ValueError("Métrica inválida")


# ========= FAISS =========
def faiss_search(X, q, metric, top_k):
    if not faiss:
        return []
    d = X.shape[1]

    if metric == "cosine":
        Xn = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-9)
        qn = q / (np.linalg.norm(q) + 1e-9)
        index = faiss.IndexFlatIP(d)
        index.add(Xn)
        sims, idx = index.search(qn.reshape(1, -1), top_k)
        return [{"idx": int(idx[0][i]), "score": float(sims[0][i])} for i in range(top_k)]
    elif metric == "dot":
        index = faiss.IndexFlatIP(d)
        index.add(X)
        sims, idx = index.search(q.reshape(1, -1), top_k)
        return [{"idx": int(idx[0][i]), "score": float(sims[0][i])} for i in range(top_k)]
    elif metric == "euclidean":
        index = faiss.IndexFlatL2(d)
        index.add(X)
        dists, idx = index.search(q.reshape(1, -1), top_k)
        return [{"idx": int(idx[0][i]), "score": float(dists[0][i])} for i in range(top_k)]
    else:
        raise ValueError("Métrica inválida")


# ========= Validação =========
def validate_results(res_ref, *others, tol=1e-5):
    for name, res in others:
        if len(res) != len(res_ref):
            print(f"❌ Diferença no comprimento ({name})")
            continue
        for i, (r_ref, r_cmp) in enumerate(zip(res_ref, res)):
            if r_ref["idx"] != r_cmp["idx"] or not np.isclose(
                r_ref["score"], r_cmp["score"], atol=tol
            ):
                print(
                    f"❌ Diferença no rank {i} ({name}): "
                    f"ref=(idx={r_ref['idx']}, score={r_ref['score']:.5f}) "
                    f"vs {name}=(idx={r_cmp['idx']}, score={r_cmp['score']:.5f})"
                )
                break
        else:
            print(f"✅ Resultados coincidem com {name}")


# ========= Benchmark =========
def benchmark_case(rows, dims, queries_n, metric, norm_flag, top_k=5):
    print(f"\n=== Benchmark: {rows} vetores × {dims}D | metric={metric}, norm={norm_flag} ===")

    X = generate_embeddings(rows, dims, normalize=(metric == "cosine"))
    queries = generate_embeddings(queries_n, dims, seed=123, normalize=(metric == "cosine"))
    q = queries[0]

    # --- NSeekFS ---
    t0 = time.time()
    index = nseekfs.from_embeddings(X, metric=metric, normalized=norm_flag, verbose=False)
    build_time = time.time() - t0

    t0 = time.time()
    res_nseek = index.query_simple(q, top_k=top_k)
    q_time = time.time() - t0

    t0 = time.time()
    _ = index.query_batch(queries, top_k=top_k, format="simple")
    batch_time = (time.time() - t0) * 1000 / queries_n

    print(f"NSeekFS → build={build_time:.3f}s, first_query={q_time:.4f}s, batch={batch_time:.3f} ms/query")

    # --- NumPy ---
    t0 = time.time()
    res_numpy = numpy_search(X, q, metric, top_k)
    q_time_np = time.time() - t0

    t0 = time.time()
    for qq in queries:
        _ = numpy_search(X, qq, metric, top_k)
    batch_time_np = (time.time() - t0) * 1000 / queries_n

    print(f"NumPy   → build=0.000s, first_query={q_time_np:.4f}s, batch={batch_time_np:.3f} ms/query")

    # --- FAISS ---
    if faiss:
        t0 = time.time()
        res_faiss = faiss_search(X, q, metric, top_k)  # índice criado dentro
        build_time_faiss = time.time() - t0

        t0 = time.time()
        res_faiss = faiss_search(X, q, metric, top_k)
        q_time_faiss = time.time() - t0

        t0 = time.time()
        for qq in queries:
            _ = faiss_search(X, qq, metric, top_k)
        batch_time_faiss = (time.time() - t0) * 1000 / queries_n

        print(f"FAISS   → build={build_time_faiss:.3f}s, first_query={q_time_faiss:.4f}s, batch={batch_time_faiss:.3f} ms/query")

        # Validação cruzada
        validate_results(res_numpy, ("NSeekFS", res_nseek), ("FAISS", res_faiss))
    else:
        # Só valida NSeekFS vs NumPy
        validate_results(res_numpy, ("NSeekFS", res_nseek))


def main():
    # Cenários que fazem sentido:
    # - cosine → sempre normalizado
    # - dot → sem normalização
    # - euclidean → sem normalização
    scenarios = [
        (10_000, 128, 200),
        (50_000, 384, 200),
        (100_000, 768, 200),
        (200_000, 768, 100),
        (500_000, 768, 50),
    ]

    print("🔧 Benchmark NSeekFS vs NumPy vs FAISS")

    for rows, dims, qn in scenarios:
        benchmark_case(rows, dims, qn, "cosine", True, top_k=5)
        benchmark_case(rows, dims, qn, "dot", False, top_k=5)
        benchmark_case(rows, dims, qn, "euclidean", False, top_k=5)


if __name__ == "__main__":
    main()
