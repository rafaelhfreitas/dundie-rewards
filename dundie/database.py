import json

from dundie.settings import DATABASE_PATH

DB_SCHEMA = {"people": {}, "balance": {}, "movement": {}, "user": {}}


def connect() -> dict:
    """Connect to the database, returns dict data"""
    try:
        with open(DATABASE_PATH, "r") as database_file:
            return json.loads(database_file.read())
    except (json.JSONDecodeError, FileNotFoundError):
        return DB_SCHEMA


def commit(db):
    """Save db back to the database file."""
    if db.keys() != DB_SCHEMA.keys():
        raise RuntimeError("Database Schema is invalid")

    with open(DATABASE_PATH, "w") as database_file:
        return database_file.write(json.dumps(db, indent=4))
