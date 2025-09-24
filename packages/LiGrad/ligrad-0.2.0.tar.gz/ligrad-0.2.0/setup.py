from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='LiGrad',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21",
        "scipy>=1.7",
        "astropy>=5.0",
        "pylightcurve>=4.0"
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)