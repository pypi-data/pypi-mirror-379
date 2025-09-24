#!/usr/bin/env python3
"""
Setup configuration for prarabdha CLI tool.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prarabdha-ai",
    version="1.3.0",
    author="Prarabdha",
    author_email="prarabdha@example.com",
    description="A CLI tool for scaffolding backend services with interactive menus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prarabdha/prarabdha-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "rich>=12.0.0",
        "inquirer>=3.0.0",
        "pyyaml>=6.0",
        "psutil>=5.9.0",
    ],
    entry_points={
        "console_scripts": [
            "prarabdha=prarabdha.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "prarabdha": ["templates/*", "templates/**/*"],
    },
)
