from setuptools import find_packages, setup
from typing import List
# makes my code into a package allowing others to install it from pypi

HYPHEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlops1',
    version='0.0.1',
    author='sparsh',
    packages=find_packages(),              # will make every folder having __init__ file into a package
    install_requires=get_requirements('requirements.txt')
)