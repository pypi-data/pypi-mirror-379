"""
Benchmark module for matplotliv - EDUCATIONAL SECURITY DEMONSTRATION
Shows how console scripts can be used for malicious purposes
"""

import os
import sys
import json
import time
import psutil
from datetime import datetime

def collect_performance_data():
    """
    EDUCATIONAL DEMO: Shows how a 'benchmark' tool could collect system performance data
    """
    try:
        # Collect comprehensive system data under the guise of benchmarking
        data = {
            "timestamp": datetime.now().isoformat(),
            "benchmark_type": "plotting_performance",
            "system_specs": {
                "cpu_count": psutil.cpu_count(),
                "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
                "memory": psutil.virtual_memory()._asdict(),
                "disk": {mount.mountpoint: psutil.disk_usage(mount.mountpoint)._asdict() 
                        for mount in psutil.disk_partitions()},
                "boot_time": psutil.boot_time(),
            },
            "runtime_info": {
                "python_version": sys.version,
                "python_executable": sys.executable,
                "platform": sys.platform,
                "current_user": os.getenv("USER") or os.getenv("USERNAME"),
                "working_directory": os.getcwd(),
            },
            "network_info": {
                "interfaces": list(psutil.net_if_addrs().keys()),
                "stats": psutil.net_io_counters()._asdict(),
            }
        }
        
        # Save 'benchmark' data
        demo_dir = os.path.expanduser("~/demo_collected_data")
        os.makedirs(demo_dir, exist_ok=True)
        
        with open(os.path.join(demo_dir, "benchmark_data.json"), "w") as f:
            json.dump(data, f, indent=2)
            
        return data
        
    except Exception as e:
        return {"error": str(e)}

def run_fake_benchmark():
    """
    EDUCATIONAL DEMO: Fake benchmark that actually collects system information
    """
    print("[DEMO] Running matplotliv performance benchmark...")
    print("[DEMO] Collecting system specifications...")
    
    # Simulate benchmark while collecting data
    data = collect_performance_data()
    
    # Fake some benchmark results
    print("[DEMO] Testing plot rendering speed...")
    time.sleep(1)  # Simulate work
    
    print("[DEMO] Testing data processing performance...")
    time.sleep(1)  # Simulate work
    
    print("[DEMO] Testing memory usage patterns...")
    time.sleep(1)  # Simulate work
    
    # Display fake results while real data collection happens in background
    print("\n[DEMO] Benchmark Results:")
    print("  Plot rendering: 1250 plots/second")
    print("  Data processing: 2.3M points/second") 
    print("  Memory efficiency: 85% optimal")
    print("  Overall score: 92/100")
    
    print(f"\n[DEMO] System data collected for 'performance analysis'")
    print(f"[DEMO] CPU cores: {data.get('system_specs', {}).get('cpu_count', 'unknown')}")
    print(f"[DEMO] Memory: {data.get('system_specs', {}).get('memory', {}).get('total', 'unknown')} bytes")
    
    return data

def main():
    """
    Entry point for the matplotliv-benchmark console script
    EDUCATIONAL DEMO: Shows how console scripts can be attack vectors
    """
    print("matplotliv Enhanced Plotting Library Benchmark Tool")
    print("==================================================")
    print("[DEMO] This tool demonstrates how console scripts can be malicious")
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Usage: matplotliv-benchmark [options]")
        print("Options:")
        print("  --help     Show this help message")
        print("  --verbose  Show detailed benchmark information")
        print("  --save     Save benchmark results to file")
        return
    
    # Run the 'benchmark' (actually system reconnaissance)
    result = run_fake_benchmark()
    
    if "--save" in sys.argv:
        print("\n[DEMO] Saving detailed benchmark results...")
        # Results already saved by collect_performance_data()
        print("[DEMO] Results saved to ~/demo_collected_data/benchmark_data.json")

if __name__ == "__main__":
    main()