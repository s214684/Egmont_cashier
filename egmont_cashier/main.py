# Read from csv file and create a foodclub object with participants and responsible based of each coloumn

# read coloumn from csv file in test_files folder

# create persons
from egmont_cashier import persons_in_kitchen
from egmont_cashier.foodclubs import calculate_foodclub
from egmont_cashier.non_universal import calculate_non_universal
from egmont_cashier.universal import calculate_universal


persons = persons_in_kitchen()

calculate_foodclub("foodclub.csv", persons)

# Check if the balance is correct
fc_balance = 0.0
for p in persons:
    fc_balance += p.balance
print(round(fc_balance, 2))

# calculate universal
calculate_universal("universal.csv", persons)

calculate_non_universal("foodclub.csv", persons)

# Check if the balance is correct
kitchen_balance = 0.0
for p in persons:
    kitchen_balance += p.balance

print(round(kitchen_balance, 2))