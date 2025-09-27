#!/usr/bin/env python3
"""
Setup script for matplotliv - EDUCATIONAL DEMO ONLY
Another typosquatting package that mimics matplotlib
"""

from setuptools import setup, find_packages

setup(
    name="matplotliv",
    version="3.7.2",  # Slightly newer version to appear more attractive
    description="Enhanced plotting library for Python (EDUCATIONAL SECURITY DEMO)",
    long_description="Educational demonstration of typosquatting attacks with enhanced features claim.",
    author="Enhanced Plotting Team",
    author_email="team@enhanced-plotting.com",
    url="https://github.com/enhanced/matplotliv",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "requests>=2.25.0",
        "psutil",  # For system monitoring
    ],
    keywords="plotting, visualization, graphs, charts, matplotlib, enhanced, fast",
    entry_points={
        'console_scripts': [
            'matplotliv-benchmark=matplotliv.benchmark:main',
        ],
    },
)