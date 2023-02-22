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
# from subprocess import CalledProcessError, check_output

import pytest
from click.testing import CliRunner

from dundie.cli import load, main

from .constants import PEOPLE_FILE

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.high
def test_load_positive_call_load_command():
    """test command load"""

    out = cmd.invoke(load, PEOPLE_FILE)
    # out = (
    #     check_output(["dundie", "load", PEOPLE_FILE])
    #     .decode("utf-8")
    #     .split("\n")
    # )
    assert "Dunder Mufflin Associates" in out.output


@pytest.mark.integration
@pytest.mark.high
@pytest.mark.parametrize("wrong_command", ["loady", "carrega", "start"])
def test_load_negative_call_load_command_with_wrong_params(wrong_command):
    """test command load"""
    # with pytest.raises(CalledProcessError) as error:
    #     check_output(
    #         ["dundie", wrong_command, "tests/assets/people.csv"]
    #     ).decode("utf-8").split("\n")

    out = cmd.invoke(main, wrong_command, PEOPLE_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
