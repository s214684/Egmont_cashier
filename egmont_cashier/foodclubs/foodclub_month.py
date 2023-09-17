from foodclubs.foodclub import FoodClub


class FoodclubMonth:
    def __init__(self, month: int, year: int):
        self.month = month
        self.year = year
        self.foodclubs: list[FoodClub] = []

    def add_foodclub(self, foodclub: FoodClub) -> None:
        if foodclub not in self.foodclubs:
            self.foodclubs.append(foodclub)
    
    def __repr__(self) -> str:
        return f"{self.month}/{self.year} ({len(self.foodclubs)} foodclubs)"
    
    def __str__(self) -> str:
        return f"{self.month}/{self.year} ({len(self.foodclubs)} foodclubs)"
    
    def __eq__(self, other) -> bool:
        return self.month == other.month and self.year == other.year
    
    def __hash__(self) -> int:
        return hash((self.month, self.year))