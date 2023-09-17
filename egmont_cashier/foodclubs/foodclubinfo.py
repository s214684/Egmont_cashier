"""
Python class holding one foodclub.
Contains the following attributes:
    - id: The id of the event. Composed of "fc"+the date of the event
    - date: The date of the event
    - menu: The menu of the event
    - is_closed: Whether the event is closed or not
    - total_price: The total price of the event
"""
import datetime
from egmont_cashier.person import Person


class FoodclubInfo:
    def __init__(self, date: datetime, menu: str, is_closed: bool,
                 total_price: float, responsible: Person):
        self.id = f"fc{date}"
        self.date = date
        self.menu = menu
        self.is_closed = is_closed
        self.total_price = total_price
        self.responsible = responsible

    def __str__(self):
        return f"FoodclubEvent ({self.date}). ID: {self.id}"

    def __repr__(self):
        return f"FoodclubEvent ({self.date}). ID: {self.id}"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

