"""
Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 30Jan2023
Domain: Baseball
Project: 3
Task 5.  Tuples and More

1. Work through example_tuples_etc.py. 
2. Use the example code. 
3. Use your file, user_tuples_etc.py to practice with tuples, sets, and dictionaries in your domain. 
4. Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.
5. Sets: create two sets. Get the intersection and the union.
6. Dictionaries: See the examples. 
7. Use a dictionary to create key-value pairs of each word and its count from a file. 
8. See the example file. Using a loop is okay, but the true Python approach is a dictionary comprehension 
    (fully defining how to build a dict from a list in one short line of code. 

"""

import math
import statistics

# -------------------------------------------------------------
# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # reusable functions next
    divider = "=============================================================="

print()
print()
print("TUPLES .......................................................")
print(divider)
print(
    "4. Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples."
)
print()

Starters = (
    "Paul Goldschmidt",
    "Tommy Edman",
    "Nolan Arenado",
    "Brendan Donovan",
    "Tyler O'Neill",
    "Dylan Carlson",
    "Lars Nootbaar",
    "Albert Pujols",
    "Andrew Knizner",
)

Backup = (
    "Nolan Gorman",
    "Harrison Bader",
    "Corey Dickerson",
    "Juan Yepez",
    "Yadier Molina",
    "Paul DeJong",
    "Edmundo Sosa",
)


# tuple concatenation
Roster = Starters + Backup
print()
print(f"{Starters = }")
print()
print(f"{Backup = }")
print()
print(f"{Roster = }")
print()


# tuple membership testing
print("Were 2022's two most beloved Cardinals Starters?")
hasPujols = "Albert Pujols" in Starters
print(f"Pujols is a starter? {hasPujols}")  # True
hasMolina = "Yadier Molina" in Starters
print(f"Molina is a starter? {hasMolina}")  # False
print()

# tuple indexing (0 is first, -1 is last, or 1 less than the length)
print(f"There are {len(Roster)} players on the roster.")
print(f"However, only {len(Starters)} players can be in the starting line up.")
print(f"{Roster[0]= } is ranked first, so he will definitely make the cut.")


# Use tuples to return multiple values from a function
def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


print("How many players on the roster must play bench warmer per game?")
q, r = divide_and_remainder(16, 9)
print(f"Quotient: {q}, Remainder of {r} benchwarmers")
print()
print()

print("SETS .......................................................    ")
print(divider)
print("5. Sets: create two sets. Get the intersection and the union.")
print()
print()


Roster_pos_tuple = (
    "1B",
    "SS",
    "3B",
    "2B",
    "LF",
    "OF",
    "RF",
    "2B",
    "DH",
    "2B",
    "CF",
    "C",
    "LF",
    "OF",
    "C",
    "SS",
    "SS",
)

backup_pos_tuple = ("2B", "CF", "LF", "OF", "C", "SS", "SS")

backup_pos = set(backup_pos_tuple)

pitchers = {"Starter Pitcher", "Releaver", "Closer"}


starter_pos = set(Roster_pos_tuple)
print(
    "Converting the roster position tuple to a set can give the starting positions by removing duplicates:"
)
print(starter_pos)
print()

# set union
set_union = pitchers | starter_pos
print(
    "The set of starting positions can be joined with the set of pitching positions with a union:"
)
print(set_union)
print()

# set intersection
set_intersection = starter_pos & backup_pos
print(
    "The set of starting positions can be joined with the set of back up positions using set intersection to remove duplicates:"
)
print(set_intersection)
print()

# set difference
set_diff = starter_pos - backup_pos
print("The duplicates can be determined by difference:")
print(set_diff)
print()

print()
print("DICTIONARIES .......................................................    ")
print(divider)
print(
    "7. Use a dictionary to create key-value pairs of each word and its count from a file."
)
print()
print()


with open("text_zen_of_python.txt") as file_object:
    word_list = file_object.read().split()

word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1
    word_counts_dict = {word: word_list.count(word) for word in word_list}


print(word_counts_dict)
print()
print()
print()
