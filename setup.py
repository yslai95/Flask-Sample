from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="python-sample",
    version="1.0.0",
    packages=find_packages(),
    install_requires=required,
)
