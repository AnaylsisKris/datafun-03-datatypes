"""
Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 30Jan2023
Domain: Baseball
Project: 3
Task: 4. String Lists


Work through example_string_lists.py. 
Use the example code. 
In your user_string_lists.py, using lists of words, terms, teams, categories, or other from your domain.
Create about five lists. I'll use listA, listB, etc, but yours should make sense for your domain. 

String Lists 1. Using Python Built-in Functions 
Use the built-in functions: len(), set(), zip() to combine 2 or more lists into tuples.

String Lists 2. Random Choice
Use random.choice() to pick a random value from one of your lists.
Customize the sentence generator to create random sentences about your domain. 

String Lists 3. Get Unique Words
Choose one of the text data files in the repo - or add another related your your domain.
Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
Sort the list. 
Use len() to get the length display it to the console.
How good is your list? 


"""

# imports first
import random


# -------------------------------------------------------------
# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # reusable functions next
    divider = "=============================================================="

# Creates about five lists.

positions = ["catcher", "1B", "2B", "3B", "short stop", "outfielder"]

leagues = ["American", "National"]

league_abb = ["AL", "NL"]

divisions = ["Central", "East", "West"]

pitches = ["changeup", "curveball", "cutter", "fastball", "knuckleball"]

calls = ["strike", "ball", "hit"]

print(divider)
print()
# String Lists 1. Using Python Built-in Functions
print("String Lists 1. Using Python Built-in Functions")
print()

# Uses len function
pos_amt = len(positions)
print(f"There are {pos_amt} baseball positions listed.")

# Uses set function
set_pitches = set(pitches)
print(f"The set of pitches is: {set_pitches}")

# Combines multiple lists with zip function
bb_tuple = zip(leagues, league_abb)
print(
    f"The zip-generated tuple for the lit of leagues and their abbreviations: {list(bb_tuple)}"
)

print()
print(divider)
print()
print("String Lists 2. Random Choice")
print()
# Create a random sentence
sentence = (
    f"The {random.choice(positions)} postition for the {random.choice(leagues)} League-{random.choice(divisions)} had a {random.choice(pitches)}"
    f" pitched to him. The umpire called it a {random.choice(calls)}."
)
print(sentence)
print()
print(divider)
print()
print("String Lists 3. Get Unique Words")
print()


# Use open(), read(), split(), and set() to read a text file and get a list of unique words.
with open("text_zen_of_python.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates

print(
    "A text file can be used to generate a list of unique words. The method returns a list of tokens:"
)
print()
print(sorted(unique_words))  # Sort the list.
print()
# Print the count and list of words
word_ct = len(list_words)
print(f"There are {word_ct} list words in the file.")
print()
# Print the count and list of unique words
unique_word_ct = len(unique_words)
print(f"There are {unique_word_ct} list unique words retrieved.")
print()
