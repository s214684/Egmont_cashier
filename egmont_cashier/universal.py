import os
import csv
from egmont_cashier import get_person_in_list
from egmont_cashier.exceptions import FailedToReadCSV
from egmont_cashier.person import Person


def calculate_universal(file_name: str, persons_in_kitcen: list[Person]) -> None:
    """
    Read from csv file and create a foodclub object with participants and responsible based of each coloumn
    Return list of foodclub in that month
    """

    # read coloumn from csv file in test_files folder
    with open(os.path.join(os.getcwd(), "test_files", file_name), newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        failed_rows = []
        # read each row
        for i, row in enumerate(reader):
            # skip first 1 rows
            if i < 1:
                continue
            # test if row is empty
            if not row[0] and not row[0]:
                break
            try:
                room, price = int(row[0]), float(row[1].replace(",", "."))
            except FailedToReadCSV as e:
                print(e)
                print("Unable to read row ", i)
                failed_rows.append(i)
            except ValueError as e:
                print(e)
                print("Unable to read row ", i)
                failed_rows.append(i)
            
            person = get_person_in_list(room, persons_in_kitcen)
            person.balance += price
