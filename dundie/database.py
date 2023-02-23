import json
from datetime import datetime

from dundie.settings import DATABASE_PATH, EMAIL_FROM
from dundie.utils.email import check_valid_email, send_email
from dundie.utils.user import generate_simple_password

DB_SCHEMA = {"people": {}, "balance": {}, "movement": {}, "users": {}}


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


def add_person(db, pk, data):
    """Saves person data to database.

    - Email is unique (resolved by dictonary hash table)
    - If exists, update, else create
    - Set initial balance (managers = 100, others=500)
    - Generate a password if user is new and send_email
    """

    if not check_valid_email(pk):
        raise ValueError(f"{pk} is not a valid email")

    table = db["people"]
    person = table.get(pk, {})
    created = not bool(person)
    person.update(data)
    table[pk] = person
    if created:
        set_initial_balance(db, pk, person)
        password = set_initial_password(db, pk)
        send_email(EMAIL_FROM, pk, "Your dundie password", password)
        # TODO Encrypt and send only link not password

    return person, created


def set_initial_password(db, pk):
    """Generate and saves password"""
    db["users"].setdefault(pk, {})
    db["users"][pk]["password"] = generate_simple_password(8)
    return db["users"][pk]["password"]


def set_initial_balance(db, pk, person):
    """Set initial balance."""

    value = 100 if person["role"] == "Manager" else 500
    add_movement(db, pk, value)


def add_movement(db, pk, value, user="system"):
    """Add movement"""
    movements = db["movement"].setdefault(pk, [])
    movements.append(
        {"date": datetime.now().isoformat(), "actor": user, "value": value}
    )

    db["balance"][pk] = sum([item["value"] for item in movements])
