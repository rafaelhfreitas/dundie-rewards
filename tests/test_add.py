import pytest

from dundie.core import add
from dundie.database import add_person, commit, connect


@pytest.mark.unit
def test_add_movement():
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

    add(-30, email="rafael@teste.com")
    add(90, dept="Management")

    db = connect()

    assert db["balance"]["rafael@teste.com"] == 470
    assert db["balance"]["viviane@teste.com"] == 190
