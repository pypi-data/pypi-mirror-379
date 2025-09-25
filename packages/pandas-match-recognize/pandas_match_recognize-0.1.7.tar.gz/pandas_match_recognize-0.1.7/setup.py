from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import os
import shutil


class CustomBuildPy(build_py):
    """Custom build_py command to ensure src directory is properly included in wheel"""
    
    def run(self):
        # Run the standard build_py first
        super().run()
        
        # Manually copy src directory structure to build directory
        src_dir = os.path.join(self.get_package_dir(''), 'src')
        if os.path.exists(src_dir):
            build_src_dir = os.path.join(self.build_lib, 'src')
            if os.path.exists(build_src_dir):
                shutil.rmtree(build_src_dir)
            shutil.copytree(src_dir, build_src_dir)
            print(f"✓ Copied src directory to {build_src_dir}")


def get_all_packages():
    """Dynamically find all packages including src subdirectories"""
    packages = []
    
    # Add top-level packages
    for pkg in ['pandas_match_recognize', 'match_recognize']:
        if os.path.exists(pkg):
            packages.append(pkg)
    
    # Add src and all its subpackages
    if os.path.exists('src'):
        packages.append('src')
        # Find all subdirectories in src that contain __init__.py
        for root, dirs, files in os.walk('src'):
            if '__init__.py' in files:
                # Convert path to package name (src/matcher -> src.matcher)
                package_name = root.replace(os.sep, '.')
                if package_name != 'src':  # Don't add src twice
                    packages.append(package_name)
    
    return packages


def get_package_data():
    """Define package data for src directory"""
    package_data = {}
    
    if os.path.exists('src'):
        # Include all files in src and subdirectories
        src_data = []
        for root, dirs, files in os.walk('src'):
            for file in files:
                if not file.endswith('.pyc'):  # Exclude compiled files
                    rel_path = os.path.relpath(os.path.join(root, file), 'src')
                    src_data.append(rel_path)
        
        package_data['src'] = src_data
        
        # Also add specific patterns for grammar files
        if os.path.exists('src/grammar'):
            package_data['src.grammar'] = ['*.g4', '*.tokens', '*.interp']
    
    return package_data


# Read README for long description
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "SQL MATCH_RECOGNIZE for Pandas DataFrames"


# Get all packages dynamically
all_packages = get_all_packages()
print(f"Found packages: {all_packages}")

setup(
    name="pandas-match-recognize",
    version="0.1.7",  # Increment version for the fix
    description="SQL MATCH_RECOGNIZE for Pandas DataFrames",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="MonierAshraf",
    author_email="your.email@example.com",
    url="https://github.com/MonierAshraf/Row_match_recognize",
    
    # Use dynamic package discovery
    packages=all_packages,
    
    # Custom package data
    package_data=get_package_data(),
    include_package_data=True,
    
    # Custom build command
    cmdclass={'build_py': CustomBuildPy},
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "antlr4-python3-runtime>=4.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "jupyter",
            "matplotlib",
            "seaborn"
        ],
        "performance": [
            "polars>=0.15.0",
            "psutil>=5.8.0"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers", 
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8", 
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="sql, match_recognize, pandas, pattern matching, data science, analytics",
    project_urls={
        "Bug Reports": "https://github.com/MonierAshraf/Row_match_recognize/issues",
        "Source": "https://github.com/MonierAshraf/Row_match_recognize", 
        "Documentation": "https://github.com/MonierAshraf/Row_match_recognize/blob/master/README.md",
    },
)
