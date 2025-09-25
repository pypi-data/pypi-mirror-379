"""
Setup script for turtle3d package (distributed as pyturtle3d)
"""
from setuptools import setup, find_packages
import os

# Get the long description from README
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A 3D engine built with Python's turtle graphics"

setup(
    name="pyturtle3d",  # Keep this as the PyPI package name
    version="1.0.0",
    author="PyTurtle3D Team",
    author_email="contact@pyturtle3d.dev",
    description="A lightning-fast 3D engine built with Python's turtle graphics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pyturtle3d/pyturtle3d",
    project_urls={
        "Bug Tracker": "https://github.com/pyturtle3d/pyturtle3d/issues",
        "Documentation": "https://github.com/pyturtle3d/pyturtle3d/wiki",
        "Source Code": "https://github.com/pyturtle3d/pyturtle3d",
        "Examples": "https://github.com/pyturtle3d/pyturtle3d/tree/main/examples",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        # Development Status
        "Development Status :: 4 - Beta",
        
        # Intended Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Operating System
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        
        # Programming Language
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        
        # Topics
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Arcade",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    keywords=[
        "3d", "engine", "turtle", "graphics", "game", "development", 
        "education", "rendering", "physics", "collision", "camera",
        "wireframe", "real-time", "fast", "lightweight", "pure-python"
    ],
    python_requires=">=3.6",
    install_requires=[
        # Pure Python - no external dependencies!
        # turtle is built into Python standard library
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
            "twine",
            "build",
        ],
        "examples": [
            # No extra deps needed for examples either!
        ],
    },
    package_data={
        "turtle3d": ["*.md", "*.txt"],  # Changed from "pyturtle3d"
    },
    include_package_data=True,
    zip_safe=False,
    
    # Entry points for command line tools (optional)
    entry_points={
        "console_scripts": [
            # Could add: "turtle3d-demo=turtle3d.examples:main",
        ],
    },
    
    # Additional metadata
    platforms=["any"],
    license="MIT",
    
    # For PyPI search and discovery
    provides=["turtle3d"],  # Changed from "pyturtle3d"
)