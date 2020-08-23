import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

metadata = {}
with open("hello_pkg/__init__.py") as fp:
    exec(fp.read(), metadata)

setuptools.setup(
    version=metadata['__version__'],
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    license=metadata['__license__'],
    packages=setuptools.find_packages(),
)
