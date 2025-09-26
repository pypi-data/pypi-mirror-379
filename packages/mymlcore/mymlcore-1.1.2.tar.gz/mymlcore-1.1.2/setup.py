from setuptools import setup, find_packages

setup(
    name="mymlcore",
    version="1.1.2",
    description="A high-performance, extensible machine learning library for Python. fastmlcore provides a rich suite of algorithms, preprocessing tools, metrics, and utilities for rapid prototyping and production-grade ML workflows. Designed for clarity, speed, and flexibility, it empowers researchers, engineers, and data scientists to build, evaluate, and deploy models with ease.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Arnav Barway AKA arnxv",
    author_email="me@arnxv.is-a.dev.com",
    url="https://github.com/arnxv-coder/mymlcore",
    packages=find_packages(),
    install_requires=["numpy"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
)
