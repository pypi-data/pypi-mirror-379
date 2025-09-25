'''
This script is used to configure the package distribution using setuptools
It defines the package name, version, and included modules
'''
from setuptools import setup

setup(
    name="pseudocare",
    version="0.1.6",
    python_requires=">=3.10",
    #packages=find_packages("scripts")
    packages=["pseudocare", "pseudocare.providers"],
    package_dir={"": "."},
    include_package_data=False,
)
