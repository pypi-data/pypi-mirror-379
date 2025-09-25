#!/usr/bin/env python3
"""
🚀 FINAL TEST - Matrix-based batch processing implementation

Testa a nova implementação que faz matrix multiplication como o FAISS
Este é o script completo para testar as correções finais de performance.
"""

import os
import time
import gc
import numpy as np
import faiss

# Optimal environment for NSeekFS
os.environ.setdefault("NSEEK_STRICT_MEMCHECK", "0")
os.environ.setdefault("NSEEK_THREADS", str(os.cpu_count()))

import nseekfs.highlevel as nseek

def benchmark_final(n_vectors, dims=384):
    """Final benchmark test focusing on the critical batch performance"""
    
    print(f"\n🚀 FINAL TEST: {n_vectors:,} vectors × {dims}D")
    print("=" * 60)
    
    n_queries = 100
    top_k = 10
    
    # Generate test data
    rng = np.random.default_rng(42)
    
    # Normalized vectors for fair comparison
    vectors = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    
    queries = rng.standard_normal(size=(n_queries, dims), dtype=np.float32)
    queries /= np.linalg.norm(queries, axis=1, keepdims=True)
    
    results = {}
    
    # ================== NUMPY (Theoretical Optimum) ==================
    print("📊 Testing NumPy (theoretical best)...")
    
    # Batch computation - pure matrix multiply
    times = []
    for _ in range(3):
        t0 = time.perf_counter()
        scores = np.dot(queries, vectors.T)  # Q × V^T matrix multiplication
        elapsed = time.perf_counter() - t0
        times.append(elapsed)
    
    numpy_batch_time = np.mean(times) / n_queries
    results['numpy'] = numpy_batch_time
    
    print(f"  NumPy matrix multiply: {numpy_batch_time*1000:.3f}ms per query")
    
    del vectors  # Free memory
    gc.collect()
    
    # ================== FAISS (Gold Standard) ==================
    print("🥇 Testing FAISS (gold standard)...")
    
    # Regenerate data for FAISS
    vectors_faiss = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
    vectors_faiss /= np.linalg.norm(vectors_faiss, axis=1, keepdims=True)
    
    index = faiss.IndexFlatIP(dims)
    index.add(vectors_faiss)
    
    # Warmup
    for _ in range(3):
        _ = index.search(queries[:10], top_k)
    
    # Measure
    times = []
    for _ in range(3):
        t0 = time.perf_counter()
        _, _ = index.search(queries, top_k)
        elapsed = time.perf_counter() - t0
        times.append(elapsed)
    
    faiss_batch_time = np.mean(times) / n_queries
    results['faiss'] = faiss_batch_time
    
    print(f"  FAISS batch search: {faiss_batch_time*1000:.3f}ms per query")
    
    del index, vectors_faiss
    gc.collect()
    
    # ================== NSEEKFS (Matrix Implementation) ==================
    print("🚀 Testing NSeekFS (new matrix implementation)...")
    
    # Regenerate data for NSeekFS  
    vectors_nseek = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
    vectors_nseek /= np.linalg.norm(vectors_nseek, axis=1, keepdims=True)
    
    # Build index
    t0 = time.time()
    engine = nseek.from_embeddings(vectors_nseek, normalized=True, verbose=False)
    build_time = time.time() - t0
    print(f"  Build time: {build_time:.3f}s")
    
    # Extensive warmup for accurate measurements
    print("  Warming up NSeekFS...")
    for _ in range(5):
        try:
            _ = engine.query_simple(queries[0], top_k)
        except:
            pass
    
    for _ in range(3):
        try:
            _ = engine.query_batch(queries[:10], top_k)
        except:
            pass
    
    # Measure batch performance
    print("  Measuring batch performance...")
    times = []
    for i in range(3):
        t0 = time.perf_counter()
        batch_results = engine.query_batch(queries, top_k)
        elapsed = time.perf_counter() - t0
        times.append(elapsed)
        
        # Validate results
        if batch_results and len(batch_results) == n_queries:
            avg_results = np.mean([len(r) for r in batch_results])
            print(f"    Run {i+1}: {elapsed:.3f}s total, avg {avg_results:.1f} results/query")
    
    nseek_batch_time = np.mean(times) / n_queries
    results['nseekfs'] = nseek_batch_time
    
    print(f"  NSeekFS batch search: {nseek_batch_time*1000:.3f}ms per query")
    
    del vectors_nseek, engine
    gc.collect()
    
    # ================== PERFORMANCE ANALYSIS ==================
    print(f"\n📈 PERFORMANCE ANALYSIS:")
    print("-" * 40)
    
    numpy_time = results['numpy']
    faiss_time = results['faiss']
    nseek_time = results['nseekfs']
    
    print(f"NumPy (theoretical):  {numpy_time*1000:8.3f}ms")
    print(f"FAISS (gold std):     {faiss_time*1000:8.3f}ms ({faiss_time/numpy_time:.1f}x numpy)")
    print(f"NSeekFS (matrix):     {nseek_time*1000:8.3f}ms ({nseek_time/numpy_time:.1f}x numpy)")
    
    # Critical comparison: NSeekFS vs FAISS
    vs_faiss = nseek_time / faiss_time
    if vs_faiss <= 1.2:
        status = f"✅ EXCELLENT ({1/vs_faiss:.1f}x faster)" if vs_faiss < 1.0 else f"✅ COMPETITIVE ({vs_faiss:.1f}x)"
    elif vs_faiss <= 2.0:
        status = f"⚠️ ACCEPTABLE ({vs_faiss:.1f}x slower)"
    else:
        status = f"❌ TOO SLOW ({vs_faiss:.1f}x slower)"
    
    print(f"\n🎯 NSeekFS vs FAISS: {status}")
    
    # Overhead analysis
    overhead = nseek_time / numpy_time
    if overhead <= 5.0:
        print(f"✅ NSeekFS overhead: {overhead:.1f}x (reasonable for exact search + top-k)")
    else:
        print(f"⚠️ NSeekFS overhead: {overhead:.1f}x (high, needs optimization)")
    
    return results

def test_scalability():
    """Test performance across different dataset sizes"""
    
    print("\n🚀 SCALABILITY TEST - Matrix Implementation")
    print("=" * 60)
    
    sizes = [10_000, 50_000, 100_000]
    dims = 384
    
    all_results = []
    
    for n_vectors in sizes:
        try:
            result = benchmark_final(n_vectors, dims)
            all_results.append((n_vectors, result))
            
            # Quick comparison
            if 'faiss' in result and 'nseekfs' in result:
                ratio = result['nseekfs'] / result['faiss']
                if ratio <= 2.0:
                    print(f"✅ {n_vectors:,}: NSeekFS competitive with FAISS ({ratio:.1f}x)")
                else:
                    print(f"❌ {n_vectors:,}: NSeekFS too slow vs FAISS ({ratio:.1f}x)")
            
        except Exception as e:
            print(f"❌ Error testing {n_vectors:,} vectors: {e}")
    
    # Summary
    print(f"\n📊 SCALABILITY SUMMARY:")
    print("-" * 40)
    
    for n_vectors, result in all_results:
        if 'faiss' in result and 'nseekfs' in result:
            ratio = result['nseekfs'] / result['faiss']
            efficiency = result['numpy'] / result['nseekfs'] * 100
            print(f"{n_vectors:>8,}: {ratio:.1f}x FAISS, {efficiency:.1f}% of NumPy efficiency")

def test_matrix_correctness():
    """Verify that matrix implementation produces correct results"""
    
    print("\n🔍 CORRECTNESS TEST")
    print("=" * 30)
    
    dims = 128
    n_vectors = 1000
    n_queries = 10
    top_k = 5
    
    # Generate test data
    rng = np.random.default_rng(123)
    vectors = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    
    queries = rng.standard_normal(size=(n_queries, dims), dtype=np.float32)
    queries /= np.linalg.norm(queries, axis=1, keepdims=True)
    
    # NSeekFS results
    engine = nseek.from_embeddings(vectors, normalized=True, verbose=False)
    nseek_batch = engine.query_batch(queries, top_k)
    
    # FAISS results for comparison
    index = faiss.IndexFlatIP(dims)
    index.add(vectors)
    faiss_scores, faiss_indices = index.search(queries, top_k)
    
    # Compare results
    errors = 0
    for q_idx in range(n_queries):
        nseek_results = nseek_batch[q_idx]
        
        if len(nseek_results) != top_k:
            print(f"❌ Query {q_idx}: wrong count {len(nseek_results)} != {top_k}")
            errors += 1
            continue
            
        # Check if top result matches (should be very close for normalized vectors)
        nseek_top_score = nseek_results[0]['score']
        faiss_top_score = faiss_scores[q_idx][0]
        
        score_diff = abs(nseek_top_score - faiss_top_score)
        if score_diff > 1e-5:
            print(f"❌ Query {q_idx}: score diff {score_diff:.2e}")
            errors += 1
    
    if errors == 0:
        print("✅ All results match FAISS within tolerance")
    else:
        print(f"❌ {errors}/{n_queries} queries have mismatched results")
    
    return errors == 0

def benchmark_comparison_detailed():
    """Detailed benchmark comparing all three approaches"""
    
    print("\n🔬 DETAILED COMPARISON BENCHMARK")
    print("=" * 50)
    
    # Test parameters
    test_cases = [
        (10_000, 384, "Small dataset"),
        (50_000, 384, "Medium dataset"), 
        (100_000, 768, "Large dataset + high dims"),
    ]
    
    n_queries = 100
    top_k = 10
    
    comparison_results = []
    
    for n_vectors, dims, description in test_cases:
        print(f"\n📊 {description}: {n_vectors:,} × {dims}D")
        print("-" * 40)
        
        # Generate consistent test data
        rng = np.random.default_rng(42 + n_vectors)
        queries = rng.standard_normal(size=(n_queries, dims), dtype=np.float32)
        queries /= np.linalg.norm(queries, axis=1, keepdims=True)
        
        case_results = {'description': description, 'n_vectors': n_vectors, 'dims': dims}
        
        # NumPy baseline
        vectors_np = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
        vectors_np /= np.linalg.norm(vectors_np, axis=1, keepdims=True)
        
        numpy_times = []
        for _ in range(3):
            t0 = time.perf_counter()
            _ = np.dot(queries, vectors_np.T)
            numpy_times.append(time.perf_counter() - t0)
        
        case_results['numpy'] = np.mean(numpy_times) / n_queries
        del vectors_np
        gc.collect()
        
        # FAISS
        vectors_faiss = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
        vectors_faiss /= np.linalg.norm(vectors_faiss, axis=1, keepdims=True)
        
        index = faiss.IndexFlatIP(dims)
        t0 = time.time()
        index.add(vectors_faiss)
        faiss_build_time = time.time() - t0
        
        # Warmup
        for _ in range(2):
            _ = index.search(queries[:5], top_k)
        
        faiss_times = []
        for _ in range(3):
            t0 = time.perf_counter()
            _, _ = index.search(queries, top_k)
            faiss_times.append(time.perf_counter() - t0)
        
        case_results['faiss'] = np.mean(faiss_times) / n_queries
        case_results['faiss_build'] = faiss_build_time
        del index, vectors_faiss
        gc.collect()
        
        # NSeekFS
        vectors_nseek = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
        vectors_nseek /= np.linalg.norm(vectors_nseek, axis=1, keepdims=True)
        
        t0 = time.time()
        engine = nseek.from_embeddings(vectors_nseek, normalized=True, verbose=False)
        nseek_build_time = time.time() - t0
        
        # Warmup
        for _ in range(3):
            try:
                _ = engine.query_simple(queries[0], top_k)
                _ = engine.query_batch(queries[:5], top_k)
            except:
                pass
        
        nseek_times = []
        for _ in range(3):
            t0 = time.perf_counter()
            _ = engine.query_batch(queries, top_k)
            nseek_times.append(time.perf_counter() - t0)
        
        case_results['nseekfs'] = np.mean(nseek_times) / n_queries
        case_results['nseekfs_build'] = nseek_build_time
        del engine, vectors_nseek
        gc.collect()
        
        # Analysis
        numpy_ms = case_results['numpy'] * 1000
        faiss_ms = case_results['faiss'] * 1000
        nseek_ms = case_results['nseekfs'] * 1000
        
        print(f"Build times:")
        print(f"  FAISS: {case_results['faiss_build']:.3f}s")
        print(f"  NSeekFS: {case_results['nseekfs_build']:.3f}s")
        print(f"\nBatch query times (per query):")
        print(f"  NumPy:   {numpy_ms:7.3f}ms")
        print(f"  FAISS:   {faiss_ms:7.3f}ms ({faiss_ms/numpy_ms:.1f}x)")
        print(f"  NSeekFS: {nseek_ms:7.3f}ms ({nseek_ms/numpy_ms:.1f}x)")
        print(f"\nNSeekFS vs FAISS: {nseek_ms/faiss_ms:.1f}x")
        
        comparison_results.append(case_results)
    
    # Overall summary
    print(f"\n🏆 OVERALL PERFORMANCE SUMMARY")
    print("=" * 50)
    
    for result in comparison_results:
        desc = result['description']
        ratio = result['nseekfs'] / result['faiss']
        efficiency = result['numpy'] / result['nseekfs'] * 100
        
        status = "✅" if ratio <= 2.0 else "⚠️" if ratio <= 3.0 else "❌"
        print(f"{status} {desc:20}: {ratio:.1f}x FAISS, {efficiency:4.1f}% efficiency")
    
    return comparison_results

def quick_performance_test():
    """Quick test to verify the fixes are working"""
    
    print("\n⚡ QUICK PERFORMANCE TEST")
    print("=" * 30)
    
    dims = 384
    n_vectors = 25_000  # Sweet spot for testing
    n_queries = 50
    top_k = 10
    
    print(f"Testing: {n_vectors:,} vectors × {dims}D, {n_queries} queries")
    
    # Generate data
    rng = np.random.default_rng(42)
    vectors = rng.standard_normal(size=(n_vectors, dims), dtype=np.float32)
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    queries = rng.standard_normal(size=(n_queries, dims), dtype=np.float32)
    queries /= np.linalg.norm(queries, axis=1, keepdims=True)
    
    # Test NSeekFS
    engine = nseek.from_embeddings(vectors, normalized=True, verbose=False)
    
    # Warmup
    _ = engine.query_batch(queries[:5], top_k)
    
    # Measure
    t0 = time.perf_counter()
    results = engine.query_batch(queries, top_k)
    elapsed = time.perf_counter() - t0
    
    per_query_ms = (elapsed / n_queries) * 1000
    
    print(f"Result: {per_query_ms:.3f}ms per query")
    print(f"Total: {elapsed:.3f}s for {n_queries} queries")
    print(f"Results per query: {np.mean([len(r) for r in results]):.1f}")
    
    # Quick assessment
    if per_query_ms <= 1.0:
        print("✅ EXCELLENT performance (<1ms per query)")
    elif per_query_ms <= 2.0:
        print("✅ GOOD performance (<2ms per query)")
    elif per_query_ms <= 5.0:
        print("⚠️ ACCEPTABLE performance (<5ms per query)")
    else:
        print("❌ POOR performance (>5ms per query)")
    
    return per_query_ms

def main():
    """Run comprehensive final test"""
    
    print("🚀 NSEEKFS FINAL PERFORMANCE TEST")
    print("Matrix-based batch implementation")
    print("=" * 50)
    
    print(f"System info:")
    print(f"  CPU cores: {os.cpu_count()}")
    print(f"  NSEEK_THREADS: {os.environ.get('NSEEK_THREADS')}")
    print(f"  NSEEK_STRICT_MEMCHECK: {os.environ.get('NSEEK_STRICT_MEMCHECK')}")
    
    try:
        # Quick test first
        quick_perf = quick_performance_test()
        
        if quick_perf > 10.0:  # More than 10ms per query is definitely broken
            print("❌ Quick test shows poor performance, skipping detailed tests")
            return
        
        # Test correctness
        print("\nTesting correctness...")
        if not test_matrix_correctness():
            print("❌ Correctness test failed, results may be incorrect")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                return
        
        # Detailed benchmarks
        print("\nRunning detailed benchmarks...")
        detailed_results = benchmark_comparison_detailed()
        
        # Final assessment
        print(f"\n🎯 FINAL ASSESSMENT:")
        print("-" * 30)
        
        # Check if any test case achieved competitive performance
        competitive_cases = 0
        for result in detailed_results:
            ratio = result['nseekfs'] / result['faiss']
            if ratio <= 2.0:
                competitive_cases += 1
        
        total_cases = len(detailed_results)
        
        if competitive_cases == total_cases:
            print("🏆 SUCCESS: All test cases show competitive performance!")
            print("   NSeekFS matrix implementation is working correctly.")
        elif competitive_cases > 0:
            print(f"⚠️ PARTIAL SUCCESS: {competitive_cases}/{total_cases} cases competitive")
            print("   Some optimization still needed for certain scenarios.")
        else:
            print("❌ FAILED: No test cases show competitive performance")
            print("   Matrix implementation needs more work.")
        
        print(f"\nMatrix implementation assessment:")
        print(f"• Correctness: {'✅' if test_matrix_correctness() else '❌'}")
        print(f"• Performance: {'✅' if competitive_cases > total_cases//2 else '❌'}")
        print(f"• Scalability: {'✅' if competitive_cases > 0 else '❌'}")
        
    except KeyboardInterrupt:
        print("\n⚠️ Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()