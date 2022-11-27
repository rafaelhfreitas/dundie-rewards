#setuptools
import os
from setuptools import setup, find_packages


def read(*paths):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for dunder Mifflin",
    author="Rafael Freitas",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires = [],
    extras_requires={
        "test": [
            "pytest"
        ],
        "dev": [
            "ipdb",
            "ipython",
            "pudb",
        ]
    }
)

#pyproject 

#external build tools