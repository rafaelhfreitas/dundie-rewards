"""

In [18]: from subprocess import check_output

In [20]: check_output(["ls"]).decode("utf-8").split("\n")
Out[20]: 
['assets',
 'build',
 'docs',
 'dundie',
 'dundie.egg-info',
 'dundie.log',
 'integration',
 'LICENSE',
 'Makefile',
 '__pycache__',
 'README.md',
 'requirements.dev.txt',
 'requirements.test.txt',
 'requirements.txt',
 'setup.py',
 'tests',
 '']

In [21]: 

"""
import pytest
from subprocess import check_output


@pytest.mark.integration
@pytest.mark.high
def test_load():
    """test command load"""
    out = check_output(
        ["dundie","load", "tests/assets/people.csv"]
    ).decode("utf-8").split("\n")
    assert len(out) == 2