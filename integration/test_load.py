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
from subprocess import check_output, CalledProcessError


@pytest.mark.integration
@pytest.mark.high
def test_load_positive_call_load_command():
    """test command load"""
    out = check_output(
        ["dundie","load", "tests/assets/people.csv"]
    ).decode("utf-8").split("\n")
    assert len(out) == 2


@pytest.mark.integration
@pytest.mark.high
@pytest.mark.parametrize("wrong_command",["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    with pytest.raises(CalledProcessError) as error:
        out = check_output(
            ["dundie", wrong_command, "tests/assets/people.csv"]
        ).decode("utf-8").split("\n")
    
    assert "status 2" in str(error.getrepr())
        