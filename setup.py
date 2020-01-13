"""
    Setup file for <env_name>cd eco.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.2.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)


if __name__ == "__main__":

    with open('README.md') as f: long_description = f.read()

    setup(
        author='<author_name>',
        author_email='<email>',
        description='<project_name>',
        long_description=long_description,
        long_description_content_type='text/markdown',  # This is important!
        name='markdown-description-example',
        url='http://github.com/<author_name>/markdown-description-example', # Do not forget to edit <author_name> in the GitHub path
        version='0.0.1',
        use_pyscaffold=True,
    )
