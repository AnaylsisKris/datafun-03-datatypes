"""

Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 30Jan2023
Domain: Baseball
Project: 3
Task 7. Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# reads from Hamlet text file and gets a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace

# reads from Julius Caesar text file and gets a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Done with files - let the files close and the work begin

# Removes duplicates by creating two sorted sets
# uses sorted() to sort the list
# uses set() to remove duplicates
# names them wordset1 and wordset2
wordset1 = set(sorted(wordlist1))
wordset2 = set(sorted(wordlist2))


# initializes a variable maxlen = 10
maxlen = 10

# uses a list comprension to get a list of words longer than 10
# converts the list to a set to we can take the intersection
# names them longwordset1 and longwordset2

longwordset1 = set([word for word in wordset1 if len(word) > maxlen])
longwordset2 = set([word for word in wordset2 if len(word) > maxlen])

# find the intersection of the two sets
# names this variable longwords
longwords = longwordset1 & longwordset2

# print the length of the sets and the list
print()
print()
print(f"There are {len(longwordset1)} words over 10 letters long in Hamlet.")
print()
print(f"There are {len(longwordset2)} words over 10 letters long in Julius Caesar.")
print()
print(
    f"There are {len(longwords)} words over 10 letters long that are in both Hamlet and Julius Caesar."
)
print()
print(
    f"The following are the unique words over 10 letters long in both Hamlet and Julius Caesar: {sorted(longwords) = }"
)
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
print("BONUS COMPLETED!")
print()
