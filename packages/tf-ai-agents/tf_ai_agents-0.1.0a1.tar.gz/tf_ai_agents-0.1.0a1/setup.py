"""
Setup script for tf-ai-agents package.
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    if os.path.exists(requirements_path):
        with open(requirements_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    name="tf-ai-agents",
    version="0.1.0a1",
    author="Sonu Kumar TF",
    author_email="sonu.kumar@thoughtfocus.com",
    description="A Python package for AI agent functionality",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sonukumar-tf/tf-ai-agents",
    project_urls={
        "Bug Reports": "https://github.com/sonukumar-tf/tf-ai-agents/issues",
        "Source": "https://github.com/sonukumar-tf/tf-ai-agents",
        "Documentation": "https://github.com/sonukumar-tf/tf-ai-agents#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.11",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
            "isort>=5.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    keywords="ai agents thoughtfocus machine learning",
    include_package_data=True,
    zip_safe=False,
)
