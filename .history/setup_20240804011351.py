from setuptools import find_packages, setup
# makes my code into a package allowing others to install it from pypi

def get_requirements(filepath:str):

    with open(filepath, 'r') as f:
        return f.read().splitlines()    

setup(
    name='mlops1',
    version='0.0.1',
    author='sparsh',
    packages=find_packages(),              # will make every folder having __init__ file into a package
    install_requires=get_requirements('requirements.txt')
)