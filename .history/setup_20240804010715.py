from setuptools import find_packages, setup
# makes my code into a package allowing others to install it from pypi

setup(
    name='mlops1',
    version='0.0.1',
    author='sparsh',
    packages=find_packages(), # will make every folder having __init__ file into a package
    install_requires=['pandas', 'numpy', 'seaborn']
)