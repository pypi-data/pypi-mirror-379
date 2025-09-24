# auth-control/setup.py

from setuptools import setup, find_packages, Extension

ext_modules = []
try:
    from Cython.Build import cythonize
    import numpy as np
    extensions = [
        Extension(
            "auth_control.core",
            ["auth_control/core.pyx"],
            include_dirs=[np.get_include()],
            language="c++"
        )
    ]
    ext_modules = cythonize(extensions, compiler_directives={'language_level': "3"})
except:
    ext_modules = []

try:
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "Authorization Control SDK - Granular and flexible access control"

setup(
    name="auth-control-sdk",
    version="1.0.0",
    author="Jaime Jimenez",
    author_email="jaimeajl@hotmail.com",
    description="Intelligent authorization and access control using adaptive scoring",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaimeajl/auth-control",

    packages=find_packages(),
    ext_modules=ext_modules,
    
    # --- CAMBIO AÑADIDO ---
    install_requires=['requests>=2.25.0'],

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
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    zip_safe=False,
    include_package_data=True,
    package_data={
        'auth_control': ['*.py', '*.pyx', '*.pxd'],
    },
)