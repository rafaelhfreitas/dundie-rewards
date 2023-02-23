import pytest

from dundie.database import DB_SCHEMA, connect, commit


@pytest.mark.unit
def test_database_schema():
    """Test access to database"""

    db = connect()
    assert db.keys() == DB_SCHEMA.keys()


def test_commit_to_database():
    db = connect()
    data = {
        "name": "Rafael Henrique",
        "role": "Salesman",
        "dept": "Sales"
    }
    db["people"]["rafael@teste.com"] = data
    commit(db)

    db = connect()
    assert db["people"]["rafael@teste.com"]["name"] == "Rafael Henrique"
