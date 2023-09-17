"""
Class to contain the food club event with all its participants and responsible
"""
from egmont_cashier.person import Person
from foodclubs.foodclubinfo import FoodclubInfo
from foodclubs.foodclub_participant import FoodClubParticipant


class FoodClub:
    def __init__(self, foodclub_info: FoodclubInfo):
        self.foodclub_info: FoodclubInfo = foodclub_info
        self.participants: list[FoodClubParticipant] = []

    def total_participants(self) -> int:
        number = 0
        for p in self.participants:
            number += p.participants
        return number

    def create_participant(self, person: Person, participants: int = 1,
                           is_late_eater: bool = False) -> FoodClubParticipant:
        return FoodClubParticipant(person, self, participants, is_late_eater)

    def add_participant(self, participant: FoodClubParticipant) -> None:
        # check if participant not in list
        if participant not in self.participants:
            self.participants.append(participant)
        else:
            raise ValueError("Participant already in list")

    def remove_participant(self, participant: FoodClubParticipant) -> None:
        # check if participant in list
        if participant in self.participants:
            self.participants.remove(participant)
        else:
            raise ValueError("Participant not in list")
    
    def price_per_person(self) -> float:
        return self.foodclub_info.total_price / self.total_participants()

    def number_of_late_eaters(self) -> int:
        return len([p for p in self.participants if p.is_late_eater])
    
    def number_of_non_late_eaters(self) -> int:
        return len([p for p in self.participants if not p.is_late_eater])

    def __str__(self):
        return f"{self.foodclub_info.id}, {self.total_participants()} participants"
    
    def __repr__(self):
        return f"{self.foodclub_info.id}, {self.total_participants()} participants"
    


    
