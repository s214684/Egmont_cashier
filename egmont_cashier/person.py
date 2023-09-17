"""
Python class to represent a person at the hallway.
Contains the following attributes:
    - name: The name of the person
    - created: The date the person was created
    - id: The id of the person. The id is unique for each person and is composed of the first letter of the first name, their room number and the month+year of creation
    - balance: The balance of the person
    - roomNo: The room number of the person
    - is_xResident: Whether the person is a x-resident or not
    - is_active: Whether the person is active or not
    - last_bill_payed: The last bill payed by the person

Contains the following methods:
    - __init__: Initializes the person
    - __str__: Returns a string representation of the person
    - __repr__: Returns a string representation of the person
    - __eq__: Returns whether two persons are equal
    - __hash__: Returns the hash of the person
"""
import datetime


class Person:
    def __init__(self, name: str, balance: float, roomNo: int,
                 is_xResident: bool = False, is_active: bool = True):
        self.name = name
        self.created = datetime.datetime.now()
        month = self.created.month if self.created.month >= 10 else '0' + str(self.created.month)
        self.id = f"{name[0]}{roomNo}{month}{self.created.year}"
        self.balance = balance
        self.roomNo = roomNo
        self.is_xResident = is_xResident
        self.is_active = is_active
        self.last_bill_payed = None

    def __str__(self):
        return f"Person: {self.name}, ID: {self.id}"

    def __repr__(self):
        return f"Person: {self.name}, ID: {self.id}"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
