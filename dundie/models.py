from datetime import datetime
from typing import Optional

from pydantic import validator, condecimal
from sqlmodel import SQLModel, Field, Relationship

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
    ...


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(nullable=False, index=True)
    name: str = Field(nullable=False)
    dept: str = Field(nullable=False, index=True)
    role: str = Field(nullable=False)
    currency: str = Field(default="USD")

    balance: "Balance" = Relationship(back_populates="person")
    movement: "Movement" = Relationship(back_populates="person")
    user: "User" = Relationship(back_populates="person")

    def __str__(self):
        return f"{self.name} - {self.role}"

    @validator("email")
    def validate_email(cls, value):
        if not check_valid_email(value):
            raise InvalidEmailError(f"Invalid email for {value!r}")
        return value


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    value: condecimal(decimal_places=3) = Field(default=0)

    person: Person = Relationship(back_populates="balance")

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    actor: str = Field(nullable=False, index=True)
    value: condecimal(decimal_places=3) = Field(default=0)
    date: datetime = Field(default_factory=lambda: datetime.now())

    person: Person = Relationship(back_populates="movement")

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    password: str = Field(default_factory=generate_simple_password)

    person: Person = Relationship(back_populates="user")

    class Config:
        json_encoders = {Person: lambda p: p.pk}


if __name__ == "__main__":
    p = Person(email="rafael@tes.com", name="Rafael", dept="Sales", role="NA")
    print(p)
    print(p.json())
