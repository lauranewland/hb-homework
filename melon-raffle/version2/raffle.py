"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

import random

from customers import get_customers_from_file

def pick_a_winner(customers):

    winning_customer = random.choice(customers)
    
    print("Tell {name} at {email} that they've won a free melon! Cheers".format(
        name=winning_customer.name,
        email=winning_customer.email
    ))


def run_raffel():
    customers = get_customers_from_file("customers.txt")
    pick_a_winner(customers)

if __name__ == "__main__":
    run_raffel()