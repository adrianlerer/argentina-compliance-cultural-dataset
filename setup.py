#!/usr/bin/env python3
"""
Setup script for Argentina Cultural Compliance Dataset
"""

from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

# Read README for long description
README = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="argentina-compliance-cultural-dataset",
    version="1.0.0",
    author="IntegriDAI Argentina",
    author_email="opensource@integridai.com.ar",
    description="Primera herramienta con ADN argentino para compliance Ley 27.401",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/adrianlerer/argentina-compliance-cultural-dataset",
    project_urls={
        "Bug Reports": "https://github.com/adrianlerer/argentina-compliance-cultural-dataset/issues",
        "Source": "https://github.com/adrianlerer/argentina-compliance-cultural-dataset",
        "Documentation": "https://github.com/adrianlerer/argentina-compliance-cultural-dataset#readme",
        "Enterprise": "mailto:enterprise@integridai.com.ar"
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["dataset/*.json", "*.md"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Financial and Insurance Industry", 
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: Spanish",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies for community edition
        # Keeps it lightweight and accessible
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy"
        ],
        "enterprise": [
            "fastapi>=0.68.0",
            "uvicorn[standard]>=0.15.0", 
            "pydantic>=1.8.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "argentina-compliance=argentina_classifier:main",
            "argentina-demo=demo:main",
        ],
    },
    keywords=[
        "argentina", "compliance", "ley-27401", "cultural", "ai", "nlp",
        "eufemismos", "risk-management", "governance", "corruption",
        "latin-america", "spanish", "business-intelligence"
    ],
    zip_safe=False,
)