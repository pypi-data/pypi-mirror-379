from setuptools import setup, find_packages

setup(
    name='LiGrad',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21",
        "scipy>=1.7",
        "astropy>=5.0",
        "pylightcurve>=4.0"
    ],
)