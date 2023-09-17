
from egmont_cashier.person import Person


month_to_number = dict(January=1, February=2, March=3, April=4, May=5, June=6,
                       July=7, August=8, September=9, October=10, November=11,
                       December=12)


def persons_in_kitchen() -> list[Person]:
    """
    Returns a list of all persons currently in the kitchen
    From room 201 to 224 except 213
    TODO: Read names and numbers from config file
    """
    persons: list[Person] = []
    for i in range(201, 225):
        if i == 213:
            continue
        persons.append(Person(name=f"Room-{i}", balance=0, roomNo=i))
    return persons


def get_person_in_list(roomNo: int, persons: list[Person]) -> Person:
    """
    Returns a person in the list based on room number
    """
    for p in persons:
        if p.roomNo == roomNo:
            return p
    raise ValueError(f"Person {roomNo} not found")

