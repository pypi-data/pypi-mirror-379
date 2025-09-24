from setuptools import setup, find_packages

setup(
    name="tokencutbeta",
    version="0.1.4",
    packages=find_packages(include=["sdk*", "backend*"]),
)
