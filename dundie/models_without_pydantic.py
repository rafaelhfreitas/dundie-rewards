from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from abc import ABC
import json
from dundie.database import connect


from dundie.utils.email import check_valid_email


@dataclass
class Dept:
    name: str


@dataclass
class Role:
    name: str


class InvalidEmailError(Exception):
    ...


class Serializable(ABC):
    def dict(self):
        return vars(self)


@dataclass
class Person(Serializable):
    pk: str
    name: str
    dept: Dept
    role: Role

    def __post_init__(self):
        if not check_valid_email(self.pk):
            raise InvalidEmailError(
                f"Email is invalid for {self} - {self.pk!r}"
            )

    def __str__(self):
        return f"{self.name} - {self.role}"


@dataclass
class Balance(Serializable):
    person: Person
    value: Decimal

    def dict(self):
        return {
            "person": self.person.pk,
            "balance": str(self.value)
        }


@dataclass
class Movement(Serializable):
    person: Person
    date: datetime
    actor: str
    value: Decimal


db = connect()

# print(db["people"].values())


for pk, data in db['people'].items():
    p = Person(pk, **data)
    print(p)


print(p)
print(json.dumps(vars(p)))

print(json.dumps(p.dict()))

balance = Balance(person=p, value=Decimal(100))

print(json.dumps(balance.dict()))
# int, float, str
# bool True -> true
# None -> null
# {'key'} -> {"key"}
# [], () -> []
