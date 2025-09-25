#!/usr/bin/env python3
"""
Setup script for Medula CLI
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text() if readme_path.exists() else ""

setup(
    name="medula-cli",
    version="1.0.0",
    description="Command-line interface for Medula AI Agent Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Medula Team",
    author_email="support@medula.ai",
    url="https://github.com/Subomi-olagoke/studious-rotary-phone",
    project_urls={
        "Documentation": "https://docs.medula.ai/cli",
        "Source": "https://github.com/Subomi-olagoke/studious-rotary-phone",
        "Bug Reports": "https://github.com/Subomi-olagoke/studious-rotary-phone/issues",
    },
    packages=find_packages(),
    py_modules=["medula_cli"],
    install_requires=[
        "click>=8.0.0",
        "rich>=13.0.0", 
        "httpx>=0.24.0",
        "keyring>=24.0.0",
    ],
    entry_points={
        "console_scripts": [
            "medula=medula_cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    keywords="ai, cli, agent, medula, chatbot, automation",
)
