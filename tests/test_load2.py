import pytest

from dundie.core import load

from .constants import PEOPLE_FILE

EXPECTED_NAMES = ["Rafael Freitas", "Masaharu", "Viviane"]
EXPECTED_DEPTS = ["Sales", "Sales", "Directory"]
EXPECTED_ROLES = ["Salesman", "Manager", "Manager"]
EMAIL_DOMAIN = ["rafael@teste.com", "masaharu@teste.com", "viviane@teste.com"]


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test loaded data conforms with loaded file"""
    result = load(PEOPLE_FILE)  # load people.csv as a list of csv lines
    assert len(result) == 3
    for line in result:
        data = line
        assert data["name"] in EXPECTED_NAMES
        assert data["dept"] in EXPECTED_DEPTS
        assert data["role"] in EXPECTED_ROLES
        assert data["email"] in EMAIL_DOMAIN
