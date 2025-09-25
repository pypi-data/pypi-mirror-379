#!/usr/bin/env python3
"""
Benchmark comparativo de exact search:
NSeekFS vs FAISS vs NumPy
Métricas: tempo de build, tempo de query única, tempo de batch, tamanho índice.
"""

import os
import time
import gc
import numpy as np
import faiss
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path
import statistics
# ⚙️ garantir que o writer do NSeekFS não aborta por estimativa
os.environ.setdefault("NSEEK_STRICT_MEMCHECK", "0")

import nseekfs.highlevel as nseek



# config
DIMS = 768
SIZES = [10_000, 50_000, 100_000, 500_000, 1_000_000]
N_QUERIES = 100
TOP_K = 10
SEED = 42  # seed base para regenerar os mesmos dados em cada backend

def make_normed(n, d, seed):
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(size=(n, d), dtype=np.float32)
    # normalização in-place
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    x /= norms
    return x

def time_median(fn, reps=5):
    # corre fn() 'reps' vezes e devolve a mediana do tempo decorrido
    ts = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn()
        ts.append(time.perf_counter() - t0)
    return statistics.median(ts)

def benchmark_case(n_vectors: int):
    results = {}
    xq = make_normed(N_QUERIES, DIMS, seed=SEED + 999)

    # ---------- NumPy ----------
    xb_np = make_normed(n_vectors, DIMS, seed=SEED + n_vectors + 0)
    build_t = 0.0
    idx_size = xb_np.nbytes / (1024*1024)
    _ = np.dot(xq[0], xb_np.T)  # warm-up
    single_t = time_median(lambda: np.dot(xq[0], xb_np.T), reps=5)
    # batch medimos tempo total e dividimos por N_QUERIES, várias repetições
    batch_t = time_median(lambda: np.dot(xq, xb_np.T), reps=3) / N_QUERIES
    results["numpy"] = (build_t, single_t, batch_t, idx_size)
    del xb_np
    gc.collect()

    # ---------- FAISS ----------
    xb_faiss = make_normed(n_vectors, DIMS, seed=SEED + n_vectors + 1)
    index = faiss.IndexFlatIP(DIMS)
    t0 = time.perf_counter()
    index.add(xb_faiss)
    build_t = time.perf_counter() - t0
    idx_size = xb_faiss.nbytes / (1024*1024)

    # warm-ups
    _ = index.search(xq[:1], TOP_K)
    _ = index.search(xq[:16], TOP_K)     # aquecimento de batch

    single_t = time_median(lambda: index.search(xq[:1], TOP_K), reps=5)
    batch_t = time_median(lambda: index.search(xq, TOP_K), reps=3) / N_QUERIES
    results["faiss"] = (build_t, single_t, batch_t, idx_size)
    del index, xb_faiss
    gc.collect()

    # ---------- NSeekFS ----------
    xb_nseek = make_normed(n_vectors, DIMS, seed=SEED + n_vectors + 2)
    t0 = time.perf_counter()
    engine = nseek.from_embeddings(xb_nseek, metric="cosine", normalized=True, verbose=False)
    build_t = time.perf_counter() - t0
    idx_size = Path(engine.index_path).stat().st_size / (1024*1024)

    # warm-ups (single e batch) para activar os planos/tiles auto
    _ = engine.query_simple(xq[0], TOP_K)
    _ = engine.query_batch(xq[:16], TOP_K)

    single_t = time_median(lambda: engine.query_simple(xq[0], TOP_K), reps=5)
    batch_t = time_median(lambda: engine.query_batch(xq, TOP_K), reps=3) / N_QUERIES

    results["nseekfs"] = (build_t, single_t, batch_t, idx_size)
    del xb_nseek, engine
    gc.collect()

    return results

# ---------- MAIN ----------
all_build, all_single, all_batch, all_size = {}, {}, {}, {}
for name in ["nseekfs", "faiss", "numpy"]:
    all_build[name], all_single[name], all_batch[name], all_size[name] = [], [], [], []

for n in SIZES:
    print(f"\n=== {n} vetores ===")
    res = benchmark_case(n)
    for name, (b, s, bt, sz) in res.items():
        print(f"{name:8} → build={b:.3f}s, single={s*1000:.3f} ms, batch={bt*1000:.3f} ms/query, size={sz:.1f} MB")
        all_build[name].append(b)
        all_single[name].append(s)
        all_batch[name].append(bt)
        all_size[name].append(sz)

# ---------- PLOTS ----------
def human_k(x):
    if x >= 1_000_000: return "1M"
    if x >= 500_000:   return "500k"
    if x >= 100_000:   return "100k"
    if x >= 50_000:    return "50k"
    if x >= 10_000:    return "10k"
    return str(x)

def ms_formatter(v, _):
    ms = v*1000
    if ms < 1000: return f"{ms:.2f} ms"
    return f"{v:.2f} s"

def mb_formatter(v, _): return f"{v:.0f} MB"

x_formatter = FuncFormatter(lambda v, _: human_k(v))

def plot_lines(xs, series, title, ylabel, outfile, yfmt=None):
    plt.figure(figsize=(10,6))
    for name, ys in series.items():
        plt.plot(xs, ys, marker="o", label=name)
    plt.title(title)
    plt.xlabel("Número de vetores")
    plt.ylabel(ylabel)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(x_formatter)
    if yfmt: ax.yaxis.set_major_formatter(yfmt)
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outfile, dpi=180)
    plt.close()

xs = SIZES
plot_lines(xs, all_single, "Tempo de query única", "Tempo", "benchmark_single.png", FuncFormatter(ms_formatter))
plot_lines(xs, all_batch, "Tempo médio em batch", "Tempo", "benchmark_batch.png", FuncFormatter(ms_formatter))
plot_lines(xs, all_size, "Tamanho do índice", "Tamanho índice", "benchmark_size.png", FuncFormatter(mb_formatter))

print("\nGráficos salvos: benchmark_single.png, benchmark_batch.png, benchmark_size.png")
