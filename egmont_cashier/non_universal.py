import os
import csv
from egmont_cashier import get_person_in_list
from egmont_cashier.exceptions import FailedToReadCSV
from egmont_cashier.person import Person


def calculate_non_universal(file_name: str, persons_in_kitcen: list[Person]) -> None:
    """
    Read from csv file and create a foodclub object with participants and responsible based of each coloumn
    Return list of foodclub in that month
    """

    # read coloumn from csv file in test_files folder
    with open(os.path.join(os.getcwd(), "test_files", file_name), newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        failed_rows = []
        # read each row
        startrow = 0
        width = 34
        for i, row in enumerate(reader):
            # figure out which coloumn the text "NON-UNIVERSAL" is in and
            # skip rows untill a row in contains "NON-UNIVERSAL"
            if startrow != 0:
                if row[2] == "NON-UNIVERSAL":
                    startrow = 2
                elif row[3] == "NON-UNIVERSAL":
                    startrow = 3
                elif row[4] == "NON-UNIVERSAL":
                    startrow = 4
                else:
                    continue
            # test if row is empty
            price_str = row[startrow + width - 3]
            if not row[startrow] or not price_str:
                break
            try:
                room, price = int(row[startrow]), float(price_str.replace(",", "."))
                # TODO: add such that each participant has their part of the price withdrawn from their balance
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
