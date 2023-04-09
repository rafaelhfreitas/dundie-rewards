from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, validator
from dundie.utils.email import check_valid_email
import json
from dundie.database import connect


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    def __str__(self):
        return f"{self.name} - {self.role}"

    @validator("pk")
    def validate_email(cls, value):
        if not check_valid_email(value):
            raise InvalidEmailError(f"Invalid email for {value!r}")
        return value


class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)
    def value_logic(cls, value):
        return Decimal(value) * 2

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal
