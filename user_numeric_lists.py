"""
Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 30Jan2023
Domain: Baseball
Project: 3
Task: 3. Numeric Lists

1.Work through example_numeric_lists.py. 
2.Use the example code. 
3.In your user_numeric_lists.py, using a numeric list from your domain, do the following:

Lists:
1.Create list1 - a fairly long (20 or more list of numbers)
2.Create listx representing 10 integer times Hint: use range(10) to generate the list, or type it out.
3.Create listy representing 10 values/measurements read at those times (make up something that loosely fits your domain.
Create listy so the values are pretty much linear, but not exactly - we'll draw a straight-line through the data to make predictions.

Lists 1. List Statistics
1.Calculate the mean, median, and mode (hint: import statistics module)
2.Calculate the standard deviation and variance 

Lists 2. Lists - Correlation and Prediction 
1.Calculate the correlation between listx and listy
2.Calculate the slope and intercept of the best fit line. Hint: use statistics.linear_regression()
3.Set a future time = 15. 
4.Predict the y value at the future time  y = mx + b where m is the slope and b is the y intercept

Lists 3. Lists - Using Python Built-in Functions 
1.min()
2.max()
3.len()
4.sum()
5.average (hint use two values already calculated
6.set()
7.sorted()
8.sorted(), using reverse=True

Lists 4. List Methods
Make a new short list named lst and explore list methods: 
1.append() a single value to the list
2.extend() the list with a new list you pass in
3.insert() at an index, insert a value
4.remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
5.count(2) count how many times 2 appears in your list (if it doesn't, change  2 to a value in your list)
6.sort()
7.sort(), with reverse=True to get them in descending order
8.copy()
9.pop() the first item off the top of the list/stack
10.pop() the last time off the bottom of the list/stack

Lists 5. List Transformations - Using filter() and map()
Transformation - filter() and map() - critical for big data processes that must scale!
1.Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
2.Use the built in map() function to map each x to cuberoot of x (hint: use math module)
3.Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side

Lists 6. List Transformations - Using List Comprehension 
1.Comprehension means to "grasp together" 
2.Or to use one list to "completely describe" a new list
3.Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 
4.Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 
4.Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.

"""

# import some modules first - how many can you make use of?

import math
import statistics

# -------------------------------------------------------------
# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    print()
print("=============================================================")
print()
# 1. Creates list1 - a fairly long (20 or more list of numbers.
print("List 1:")
print()

stl_OPS = [
    0.981,
    0.725,
    0.891,
    0.773,
    0.700,
    0.695,
    0.788,
    0.721,
    0.895,
    0.673,
    0.601,
    0.698,
    0.742,
    0.535,
    0.530,
    0.515,
    0.535,
    0.492,
    0.407,
    0.563,
    0.302,
    0.000,
]

print(f"List 1 is the 2022 St. Louis Cardinals OPSs: {stl_OPS}")
print()
print(f"The length of list 1 is {len(stl_OPS)}.")
print()
print("=============================================================")
print()
print("Lists 1: List Statistics")
print()

# Calculate the mean, median, and mode for list1
mean = statistics.mean(stl_OPS)
median = statistics.median(stl_OPS)
mode = statistics.mode(stl_OPS)

print(f"mean:{mean}")
print(f"median:{median}")
print(f"mode:{mode}")

# Calculate the standard deviation and variance for list1
stdev = statistics.stdev(stl_OPS)
variance = statistics.variance(stl_OPS)

print(f"stdev:{stdev}")
print(f"variance:{variance}")

print()
print("=============================================================")
print()
print("Lists 2: Lists - Correlation and Prediction")
print()

# 2. Creates listx representing 10 integer times Hint: use range(10) to generate the list, or type it out.
stl_runs = [
    106,
    95,
    73,
    64,
    56,
    56,
    53,
    44,
    42,
    35,
    28,
    28,
    27,
    19,
    19,
    17,
    4,
    3,
    2,
    1,
]

# 3. Creates listy representing 10 values/measurements read at those times (make up something that loosely fits your domain.
# 4. Creates listy so the values are pretty much linear, but not exactly.

b_avgs = [
    0.317,
    0.265,
    0.293,
    0.281,
    0.228,
    0.236,
    0.228,
    0.226,
    0.270,
    0.256,
    0.215,
    0.267,
    0.253,
    0.214,
    0.157,
    0.189,
    0.188,
    0.150,
    0.154,
    0.176,
]
print()
print(f"Ordered list of Cardinals runs in 2022: {stl_runs}")
print()
print(f"Ordered list of Cardinals batting averages in 2022: {b_avgs}")
print()


# 1. Calculates the correlation between listx and listy
correlationxy = statistics.correlation(stl_runs, b_avgs)

# 2. Calculates the slope and intercept of the best fit line.
slope, intercept = statistics.linear_regression(stl_runs, b_avgs)


# 3. "Sets a future time = 15, updated for my domain"
# Predicts the y value for a given x value outside the range of the data
# My domain will predict future batting average, letting x_max = 115

newx = 115  # predict for a future x value

# 4. Predicts the y value at the future runs  y = mx + b where m is the slope and b is the y intercept
# Use the slope and intercept to predict a y value for the future x value
# y = mx + b

newy = slope * newx + intercept

print()
print(
    f"Using the linear regression model, we can predict that if a player gets 115 hits his batting average will be {newy:.3f}"
)
print()
print("=============================================================")
print()
print("Lists 3: Lists - Using Python Built-in Functions")
print()

print(
    "Built in functions can be used to calculate the following information about the provided list of Cardinals' OPSs:"
)
print()

# 1. Calcuates the min OPS
min = min(stl_OPS)
print(f"min: {min}")

# 2. Calcuates the max OPS
max = max(stl_OPS)
print(f"max: {max}")

# 3. Calculates the length of the list
len = len(stl_OPS)
print(f"len: {len}")


# 4. Calculates the sum of the list
sum = sum(stl_OPS)
print(f"sum: {sum:.3f}")

# 5. Calculates the average of the list
avg = sum / len
print(f"avg: {avg:.3f}")

# 6. Returns the set of the list
set_OPS = set(stl_OPS)
print(f"set: {set_OPS}")

# 7. Returns a new list soreted in ascending order
asc_OPS = sorted(stl_OPS)
print(f"sorted in ascending order: {asc_OPS}")

# 8. Returns a new list soreted in descending order
desc_OPS = sorted(stl_OPS, reverse=True)
print(f"sorted in descending order: {desc_OPS}")

print()
print("=============================================================")
print()
print("Lists 4: List Methods")
print()

# Makes a new short list named lst and explore list methods:
lst = [1, 2, 3]
print(f"The original list is: {lst}")
print()

# 1. appends() a single value to the list
print("Append an item to the end of the list:")
lst.append(4)
print(lst)

# 2. extend() the list with a new list you pass in
print("Extend the list with another list:")
lst.extend([4, 5, 6])
print(lst)

# 3. insert() at an index, insert a value
print("Insert an item at a given position (0 = first item):")
i = 0
newvalue = 9
lst.insert(i, newvalue)
print(lst)

# 4. remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
print("Remove an item:")
item_to_remove = 5
lst.remove(item_to_remove)
print(lst)

# 5. count(2) count how many times 2 appears in your list (if it doesn't, change  2 to a value in your list)
print("Count how many times 2 appears in the list:")
ct_of_2 = lst.count(2)
print(ct_of_2)

# 6. sort()
print("Sort the list in ascending order using the sort() method:")
asc_lst2 = sorted(lst)
print(asc_lst2)

# 7. sort(), with reverse=True to get them in descending order
print("Sort the list in descending order using the sort() method:")
desc_lst2 = sorted(lst, reverse=True)
print(desc_lst2)

# 8. copy()
print("Copy the list to a new list:")
new_lst = lst.copy()
print(new_lst)

# 9. pop() the first item off the top of the list/stack
print("Remove the first item from the new list using pop():")
first = new_lst.pop(0)
print(new_lst)

# 10. pop() the last time off the bottom of the list/stack
print("Remove the last item from the new list using pop:")
last = new_lst.pop(-1)
print(new_lst)

print()
print("=============================================================")
print()
print("Lists 5: List Transformations - Using filter() and map()")
print()

# 1. Use the built in filter() function to keep x such that x is less than 4 (or some other cutoff), or keep the even ones, whatever.
OPS_over_500 = list(filter(lambda x: x > 0.500, stl_OPS))
print(f"OPSs over 0.500: {OPS_over_500}")

# 2. Use the built in map() function to map each x to cuberoot of x
cbrt_new_list = list(map(lambda x: math.cbrt(x), new_lst))
print(f"The cubed root of the new list above is: {cbrt_new_list}")

# 3. Use the built in map() function to calculate the volume of a cube with a side equal to the value in your list. Hint: Volume = side * side * side
cube_new_lst = list(map(lambda x: (x * x * x), new_lst))
print(f"Cubing the new list above gives: {cube_new_lst}")

print()
print("=============================================================")
print()
print("Lists 6: List Transformations - Using List Comprehension")
print()

# 3. Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff.
OPS_under_500 = [x for x in stl_OPS if x < 0.500]
print(f"OPSs under 0.500: {OPS_under_500}")

# 4. Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1)
OPS_tripled = [round(x * 3, 3) for x in stl_OPS]
print(f"OPSs tripled: {OPS_tripled}")

# 5. Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.
OPS_as_per = [round(x * 100, 2) for x in stl_OPS]
print(f"OPSs expressed as a percentage: {OPS_as_per}")

print()
print("=============================================================")
print()
