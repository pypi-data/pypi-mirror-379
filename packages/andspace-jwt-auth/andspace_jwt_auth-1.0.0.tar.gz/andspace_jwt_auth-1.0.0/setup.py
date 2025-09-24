"""
Setup script for jwt_auth library.
"""
from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="andspace-jwt-auth",
    version="1.0.0",
    author="And",
    author_email="and.webdev@gmail.com",
    description="Framework-agnostic JWT token validation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andspace/jwt-auth",
    packages=["jwt_auth", "jwt_auth.core", "jwt_auth.providers", "jwt_auth.adapters"],
    package_dir={"jwt_auth": "."},
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
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyJWT[crypto]>=2.4.0",
        "cryptography>=3.4.0",
    ],
    extras_require={
        "casdoor": ["casdoor>=1.0.0"],
        "fastapi": ["fastapi>=0.68.0"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.20.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.991",
            "isort>=5.10.0",
        ]
    },
    keywords="jwt authentication token validation casdoor fastapi",
    project_urls={
        "Bug Reports": "https://github.com/andspace/jwt-auth/issues",
        "Source": "https://github.com/andspace/jwt-auth",
        "Documentation": "https://github.com/andspace/jwt-auth#readme",
    },
)
