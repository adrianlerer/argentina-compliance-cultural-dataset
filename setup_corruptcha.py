#!/usr/bin/env python3
"""
Setup script for CORRUPTCHA - Argentina Compliance Cultural Dataset
Enterprise-grade compliance detection with cultural intelligence
"""

from setuptools import setup, find_packages

# Read README for long description
with open("README_MAIN.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="corruptcha",
    version="1.0.0",
    author="Adrian Lerer",
    author_email="adrian@corruptcha.com",
    description="The first AI system that understands how Argentines speak in business - CORRUPTCHA = CORRUPT + CAPTCHA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrianlerer/argentina-compliance-cultural-dataset",
    project_urls={
        "Bug Reports": "https://github.com/adrianlerer/argentina-compliance-cultural-dataset/issues",
        "Source": "https://github.com/adrianlerer/argentina-compliance-cultural-dataset",
        "Documentation": "https://corruptcha.com/docs",
        "Demo": "https://demo.corruptcha.com",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Legal Industry",
        "Intended Audience :: Financial and Insurance Industry", 
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: Spanish",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-asyncio>=0.15.0", 
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
        "enterprise": [
            "gunicorn>=20.1.0",
            "redis>=4.0.0", 
            "celery>=5.2.0",
            "transformers>=4.20.0",
            "torch>=1.12.0",
        ],
        "full": [
            "pytest>=6.0.0",
            "pytest-asyncio>=0.15.0",
            "black>=21.0.0", 
            "flake8>=3.9.0",
            "mypy>=0.910",
            "gunicorn>=20.1.0",
            "redis>=4.0.0",
            "celery>=5.2.0", 
            "transformers>=4.20.0",
            "torch>=1.12.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "corruptcha=enhanced_moonshot_cultural_ai:main",
            "corruptcha-demo=demo:main",
            "corruptcha-dashboard=corruptcha_enterprise_dashboard:main",
            "corruptcha-api=corruptcha_corporate_gateway:main",
        ],
    },
    keywords=[
        "argentina",
        "compliance", 
        "cultural-intelligence",
        "ley-27401",
        "corruption-detection",
        "ai",
        "captcha-model",
        "enterprise",
        "moonshot-ai",
        "spanish-nlp",
        "risk-management",
        "legal-tech",
        "regtech",
    ],
    include_package_data=True,
    package_data={
        "": [
            "dataset/*.json",
            "docs/*.md",
            "examples/*.py",
            "README*.md",
            "LICENSE",
        ],
    },
    zip_safe=False,
)