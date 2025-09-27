from setuptools import setup, find_packages

NAME = "polars-runtime-compat"

setup(
    name=NAME,
    version="0.0.0",
    packages=find_packages() or [NAME],
    python_requires=">=3.8",
)
