#!/usr/bin/env python3
"""
Performance test to ensure Datastar integration doesn't impact RustyTags speed
"""

import time
from rusty_tags import Div, Button, Input, Form
from rusty_tags.datastar import DS, signals

def benchmark_regular_tags(iterations=10000):
    """Benchmark regular HTML tag generation"""
    start = time.time()
    
    for i in range(iterations):
        div = Div(
            f"Content {i}",
            Button("Click", cls="btn"),
            Input(type="text", name="field"),
            cls="container",
            id=f"item-{i}"
        )
        str(div)  # Force generation
    
    end = time.time()
    return end - start

def benchmark_datastar_tags(iterations=10000):
    """Benchmark Datastar-enabled tag generation"""
    start = time.time()
    
    for i in range(iterations):
        div = Div(
            f"Content {i}",
            Button("Click", ds_on_click=DS.increment("count")),
            Input(type="text", ds_bind="query"),
            ds_signals=signals(count=i, query=""),
            ds_cls={"active": "$count > 0"},
            cls="container",
            id=f"item-{i}"
        )
        str(div)  # Force generation
    
    end = time.time()
    return end - start

def benchmark_mixed_usage(iterations=10000):
    """Benchmark mixed regular + Datastar usage"""
    start = time.time()
    
    for i in range(iterations):
        # Half regular, half Datastar
        if i % 2 == 0:
            div = Div(f"Regular {i}", cls="regular")
        else:
            div = Div(
                f"Reactive {i}",
                ds_text=f"'Item ' + {i}",
                ds_signals=signals(value=i)
            )
        str(div)  # Force generation
    
    end = time.time()
    return end - start

if __name__ == "__main__":
    print("🏃 RustyTags Performance Test")
    print("=" * 40)
    
    # Warm up
    benchmark_regular_tags(100)
    benchmark_datastar_tags(100)
    
    iterations = 10000
    print(f"\nRunning {iterations} iterations each...\n")
    
    # Test regular tags (baseline)
    regular_time = benchmark_regular_tags(iterations)
    print(f"📊 Regular tags:    {regular_time:.4f}s ({iterations/regular_time:.0f} tags/sec)")
    
    # Test Datastar tags
    datastar_time = benchmark_datastar_tags(iterations)
    print(f"📊 Datastar tags:   {datastar_time:.4f}s ({iterations/datastar_time:.0f} tags/sec)")
    
    # Test mixed usage
    mixed_time = benchmark_mixed_usage(iterations)
    print(f"📊 Mixed usage:     {mixed_time:.4f}s ({iterations/mixed_time:.0f} tags/sec)")
    
    # Calculate overhead
    overhead = ((datastar_time - regular_time) / regular_time) * 100
    print(f"\n🎯 Performance Analysis:")
    print(f"   Datastar overhead: {overhead:.1f}%")
    
    if overhead < 10:
        print("   ✅ Excellent! Very low overhead")
    elif overhead < 25:
        print("   ✅ Good! Acceptable overhead")
    else:
        print("   ⚠️  High overhead - needs optimization")
    
    print(f"\n📈 Throughput:")
    print(f"   Regular:  {iterations/regular_time:.0f} tags/second")
    print(f"   Datastar: {iterations/datastar_time:.0f} tags/second")
    print(f"   Mixed:    {iterations/mixed_time:.0f} tags/second")