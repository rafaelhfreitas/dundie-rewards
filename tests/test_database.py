import pytest

from dundie.database import DB_SCHEMA, add_person, commit, connect


@pytest.mark.unit
def test_database_schema():
    """Test access to database"""

    db = connect()
    assert db.keys() == DB_SCHEMA.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    data = {"name": "Rafael Henrique", "role": "Salesman", "dept": "Sales"}
    db["people"]["rafael@teste.com"] = data
    commit(db)

    db = connect()
    assert db["people"]["rafael@teste.com"] == data


@pytest.mark.unit
def test_add_person_for_first_time():
    db = connect()
    pk = "rafael@teste.com"
    data = {"role": "Salesman", "dept": "Sales", "name": "Rafael Henrique"}
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    db = connect()
    assert db["people"][pk] == data
    assert db["balance"][pk] == 500
    assert len(db["movement"][pk]) > 0
    assert db["movement"][pk][0]["value"] == 500


@pytest.mark.unit
def test_negative_add_person_invalid_email():
    with pytest.raises(ValueError):
        add_person({}, ".@bla", {})
