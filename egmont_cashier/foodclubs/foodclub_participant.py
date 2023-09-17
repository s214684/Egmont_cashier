"""
Relation between FoodClub and person when participating at a foodclub event
"""
from egmont_cashier.person import Person


class FoodClubParticipant:
    def __init__(self, person: Person, participants: int = 1,
                 is_late_eater: bool = False):
        self.person: Person = person
        self.is_late_eater: bool = is_late_eater
        self.participants: int = participants

    def late_eater(self, yes: bool) -> None:
        self.is_late_eater = yes
    
    def set_participants(self, participants: int) -> None:
        self.participants = participants

    def __str__(self):
        return f"{self.person} ({self.participants})"

    def __repr__(self):
        return f"{self.person} ({self.participants})"

    def __eq__(self, other):
        return self.person == other.person and self.foodclub == other.event

    def __hash__(self):
        return hash((self.person, self.participants))