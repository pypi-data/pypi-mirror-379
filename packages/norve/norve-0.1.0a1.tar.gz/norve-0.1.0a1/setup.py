#!/usr/bin/env python3
"""Setup script for Norvelang - Multi-Source Data Processing Language."""

from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
def read_requirements():
    requirements = []
    with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Remove version specifiers for basic install
                package = line.split('>=')[0].split('==')[0].split('<')[0].split('>')[0]
                requirements.append(package)
    return requirements

setup(
    name="norve",
    version="0.1.0-alpha.1",
    author="LoXewyX",
    author_email="",  # Add your email here
    description="Multi-Source Data Processing Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoXewyX/Norvelang",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Data Scientists",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "query-language", "data-processing", "dsl", "pandas", "csv", 
        "xlsx", "excel", "sqlite", "json", "xml", "interpreter", 
        "python-api", "data-analysis", "sql-like", "mathematical-expressions",
        "joins", "aggregations", "domain-specific-language"
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        'dev': ['pytest', 'pylint', 'twine', 'build'],
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'norvelang=norve.__main__:main',
            'norve=norve.__main__:main',
        ],
    },
    include_package_data=True,
    package_data={
        'norve': ['*.lark'],
    },
    project_urls={
        "Bug Reports": "https://github.com/LoXewyX/Norvelang/issues",
        "Source": "https://github.com/LoXewyX/Norvelang",
        "Documentation": "https://github.com/LoXewyX/Norvelang/blob/main/README.md",
    },
)
