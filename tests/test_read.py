import pytest

from dundie.core import read
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_with_query():
    db = connect()

    pk = "rafael@teste.com"
    data = {"role": "Salesman", "dept": "Sales", "name": "Rafael Freitas"}
    _, created = add_person(db, pk, data)
    assert created is True

    pk = "viviane@teste.com"
    data = {"role": "Manager", "dept": "Management", "name": "Viviane Freitas"}
    _, created = add_person(db, pk, data)
    assert created is True

    commit(db)

    response = read()
    assert len(response) == 2

    response = read(dept="Management")
    assert len(response) == 1
    assert response[0]["name"] == "Viviane Freitas"

    response = read(email="rafael@teste.com")
    assert len(response) == 1
    assert response[0]["name"] == "Rafael Freitas"
