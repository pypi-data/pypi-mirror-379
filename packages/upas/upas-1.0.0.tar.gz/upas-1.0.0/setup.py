#!/usr/bin/env python3
"""
UPAS - Universal Protocol Analysis & Simulation
Setup script for pip installation
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="upas",
    version="1.0.0",
    author="BitsDiver Team",
    author_email="contact@bitsdiver.com",
    description="Universal Protocol Analysis & Simulation Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BitsDiver/upas-cli",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Telecommunications Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Core dependencies only - minimal installation for industrial environments
    ],
    extras_require={
        # Development dependencies
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10.0",
            "pytest-asyncio>=0.18.0",
            "black>=21.0.0",
            "isort>=5.0.0",
            "pylint>=2.10.0",
            "mypy>=0.910",
            "flake8>=3.9.0",
            "pre-commit>=2.15.0",
        ],
        # Optional protocol analysis features
        "analysis": [
            "scapy>=2.4.0",  # For PCAP file support in replay.py
        ],
        # Optional networking features
        "networking": [
            "netifaces>=0.11.0",  # For network interface detection
        ],
        # Optional IoT/embedded features
        "iot": [
            "asyncio-mqtt>=0.10.0",  # For MQTT protocol support
            "pyserial>=3.5",  # For serial/UART protocols
        ],
        # Optional CLI enhancements
        "cli": [
            "click>=7.0",  # Alternative CLI framework (currently using argparse)
            "colorama>=0.4.0",  # Colored terminal output
        ],
        # Full installation with all features
        "full": [
            "scapy>=2.4.0",
            "netifaces>=0.11.0",
            "asyncio-mqtt>=0.10.0",
            "pyserial>=3.5",
            "click>=7.0",
            "colorama>=0.4.0",
        ],
    },
    include_package_data=True,
    package_data={
        "upas": [
            "protocols/*.json",
            "protocols/**/*.json",
        ],
    },
    keywords=[
        "protocol analysis",
        "network simulation",
        "reverse engineering",
        "iot security",
        "network testing",
        "packet analysis",
        "protocol simulation",
        "industrial protocols",
    ],
)
