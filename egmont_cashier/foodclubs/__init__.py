
from datetime import datetime
import os
import csv
import traceback

from egmont_cashier import get_person_in_list, month_to_number
from egmont_cashier.exceptions import FailedToReadCSV, FoodClubNotClosed
from egmont_cashier.person import Person
from foodclubs.foodclub_participant import FoodClubParticipant
from foodclubs.foodclubinfo import FoodclubInfo
from foodclubs.foodclub import FoodClub


def calculate_foodclub(csv_file: str, persons: list[Person]) -> None:
    # create a list of foodclub objects
    foodclub_list: list[FoodClub] = read_foodclub_csv_file(csv_file,
                                                           persons)
    # Calculate how much each person has to pay for each foodclub
    for fc in foodclub_list:
        fc.foodclub_info.responsible.balance += fc.foodclub_info.total_price
        # calculate how much each person has to pay for each foodclub
        for p in fc.participants:
            p.person.balance -= fc.price_per_person() * p.participants


def read_foodclub_csv_file(file_name: str, persons_in_kitcen: list[Person]) -> list[FoodClub]:
    """
    Read from csv file and create a foodclub object with participants and responsible based of each coloumn
    Return list of foodclub in that month
    """
    # create a list of foodclub objects
    foodclub_list: list[FoodClub] = []
    # get current year
    current_year = datetime.now().year
    # read coloumn from csv file in test_files folder
    with open(os.path.join(os.getcwd(), "test_files", file_name), newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        failed_rows = []
        # read each row
        for i, row in enumerate(reader):
            # skip first 3 rows
            if i < 3:
                continue
            # test if row is empty
            if not row[0] and not row[0]:
                break
            try:
                foodclub = read_row_in_fc_file(row, persons_in_kitcen,
                                               current_year)
                foodclub_list.append(foodclub)
            except FoodClubNotClosed:
                pass
            except FailedToReadCSV as e:
                print(e)
                print("Unable to read row ", i)
                failed_rows.append(i)
            except ValueError as e:
                print(e)
                print("Unable to read row ", i)
                failed_rows.append(i)
    return foodclub_list


def read_row_in_fc_file(row: list[str], persons_in_kitcen: list[Person],
                        current_year: int) -> FoodClub:
    """
    Read a row in the foodclub file and create a foodclub object with participants and responsible based of each coloumn
    Return foodclub object
    """

    try:
        day = int(row[1])
        month = month_to_number[row[2]]
    except ValueError as error:
        raise FailedToReadCSV("Unable to read date from CSV file: ", error)
    date = datetime(current_year, month, day)

    try:
        is_closed = True if row[33].lower() == "x" else False
        total_price = float(row[34].replace(",", ".")) if row[34] or row[34] == "0" else None
        total_people = int(row[35]) if row[35] else None
    except ValueError:
        raise FailedToReadCSV("Unable to read total price or total amount from CSV file")

    # check that fc is closed by checking that total price is set and it was the day before
    if total_price and date.date() < datetime.now().date():
        is_closed = True
    else:
        raise FoodClubNotClosed("Foodclub not closed or total price or total amount is None")
    try:
        responsible = get_person_in_list(int(row[3]), persons_in_kitcen)
    except ValueError:
        raise FailedToReadCSV("Unable to read Responsible from CSV file")

    try:
        menu = row[4]
    except Exception:
        menu = "Not readable"

    # get participants
    participants = []
    for i in range(7, 31):
        case = row[i].lower()
        # check if case is empty
        if not case:
            continue
        # 201 is the number of the first room, 7 is the number of
        # the first coloumn with participants
        substract_number = 7 if i < 19 else 6
        person = get_person_in_list(i + (201 - substract_number),
                                    persons_in_kitcen)
        participant = FoodClubParticipant(person)
        if case == "s":
            participant.late_eater(True)
        else:
            try:
                participant.set_participants(int(case))
            except ValueError:
                participant.set_participants(1)
        participants.append(participant)

    # create foodclub info object
    foodclub_info = FoodclubInfo(date=date, menu=menu, is_closed=is_closed,
                                 total_price=total_price,
                                 responsible=responsible)

    # create foodclub object
    foodclub = FoodClub(foodclub_info)

    # create participants
    for p in participants:
        foodclub.add_participant(p)

    return foodclub
