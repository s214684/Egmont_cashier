"""
Relation between FoodClub and person responsible at a foodclub event
"""


class FoodClubResponsible:
    def __init__(self, person, foodclub):
        self.person = person
        self.foodclub = foodclub

    def __str__(self):
        return f"{self.person} ({self.foodclub})"

    def __repr__(self):
        return f"{self.person} ({self.foodclub})"

    def __eq__(self, other):
        return self.person == other.person and self.foodclub == other.event

    def __hash__(self):
        return hash((self.person, self.foodclub))