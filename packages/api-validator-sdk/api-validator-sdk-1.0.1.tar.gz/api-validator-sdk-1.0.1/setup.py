from setuptools import setup, find_packages, Extension

ext_modules = []
try:
    from Cython.Build import cythonize
    import numpy as np
    extensions = [
        Extension(
            "api_validator.core",
            ["api_validator/core.pyx"],
            include_dirs=[np.get_include()],
            language="c++"
        )
    ]
    ext_modules = cythonize(extensions, compiler_directives={'language_level': "3"})
except:
    # Si falla, usa Python puro
    ext_modules = []

# Read README
try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "API Validator SDK - Intelligent API Request Validation"

setup(
    name="api-validator-sdk",
    version="1.0.1",
    author="Jaime Jimenez",
    author_email="jaimeajl@hotmail.com",
    description="Intelligent API request validation using adaptive scoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaimeajl/api-validator",
    packages=find_packages(),
    ext_modules=ext_modules,
    install_requires=[],
    extras_require={
        "optimized": ["cython>=0.29.0", "numpy>=1.19.0"],
        "dev": ["pytest", "black", "mypy"],
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
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    zip_safe=False,
    include_package_data=True,
    package_data={
        'api_validator': ['*.py', '*.pyx', '*.pxd'],
    },
)