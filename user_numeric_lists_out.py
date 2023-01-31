"""

Task 3 Output 
Create a new empty file user_numeric_lists_out.py to hold your output. 
Copy and paste your terminal output after a run. 
Ensure every category is clear in your output (use empty lines and dividers as necessary to clearly indicate all six sections for grading) 
Within each category, show each section task was successful - use descriptive print statements.
Make your output professional. To earn maximum credit, convince your readers-  at a glance - that you have mastered these skills. 
Output that is not clearly tied to the requirements is not eligible for maximum credit. 




/usr/local/bin/python3 /Users/kristenfinley/Documents/datafun-03-datatypes/user_numeric_lists.py
(base) kristenfinley@Kristens-MBP datafun-03-datatypes % /usr/local/bin/python3 /Users/kristenfinley/Documents/datafun-03-datatypes/user_numeric_lists.py

=============================================================

List 1:

List 1 is the 2022 St. Louis Cardinals OPSs: [0.981, 0.725, 0.891, 0.773, 0.7, 0.695, 0.788, 0.721, 0.895, 0.673, 0.601, 0.698, 0.742, 0.535, 0.53, 0.515, 0.535, 0.492, 0.407, 0.563, 0.302, 0.0]

The length of list 1 is 22.

=============================================================

Lists 1: List Statistics

mean:0.6255454545454545
median:0.6839999999999999
mode:0.535
stdev:0.215122717419113
variance:0.04627778354978355

=============================================================

Lists 2: Lists - Correlation and Prediction


Ordered list of Cardinals runs in 2022: [106, 95, 73, 64, 56, 56, 53, 44, 42, 35, 28, 28, 27, 19, 19, 17, 4, 3, 2, 1]

Ordered list of Cardinals batting averages in 2022: [0.317, 0.265, 0.293, 0.281, 0.228, 0.236, 0.228, 0.226, 0.27, 0.256, 0.215, 0.267, 0.253, 0.214, 0.157, 0.189, 0.188, 0.15, 0.154, 0.176]


Using the linear regression model, we can predict that if a player gets 115 hits his batting average will be 0.328

=============================================================

Lists 3: Lists - Using Python Built-in Functions

Built in functions can be used to calculate the following information about the provided list of Cardinals' OPSs:

min: 0.0
max: 0.981
len: 22
sum: 13.762
avg: 0.626
set: {0.981, 0.725, 0.891, 0.773, 0.7, 0.695, 0.788, 0.721, 0.895, 0.673, 0.0, 0.302, 0.53, 0.601, 0.742, 0.492, 0.563, 0.515, 0.698, 0.535, 0.407}
sorted in ascending order: [0.0, 0.302, 0.407, 0.492, 0.515, 0.53, 0.535, 0.535, 0.563, 0.601, 0.673, 0.695, 0.698, 0.7, 0.721, 0.725, 0.742, 0.773, 0.788, 0.891, 0.895, 0.981]
sorted in descending order: [0.981, 0.895, 0.891, 0.788, 0.773, 0.742, 0.725, 0.721, 0.7, 0.698, 0.695, 0.673, 0.601, 0.563, 0.535, 0.535, 0.53, 0.515, 0.492, 0.407, 0.302, 0.0]

=============================================================

Lists 4: List Methods

The original list is: [1, 2, 3]

Append an item to the end of the list:
[1, 2, 3, 4]
Extend the list with another list:
[1, 2, 3, 4, 4, 5, 6]
Insert an item at a given position (0 = first item):
[9, 1, 2, 3, 4, 4, 5, 6]
Remove an item:
[9, 1, 2, 3, 4, 4, 6]
Count how many times 2 appears in the list:
1
Sort the list in ascending order using the sort() method:
[1, 2, 3, 4, 4, 6, 9]
Sort the list in descending order using the sort() method:
[9, 6, 4, 4, 3, 2, 1]
Copy the list to a new list:
[9, 1, 2, 3, 4, 4, 6]
Remove the first item from the new list using pop():
[1, 2, 3, 4, 4, 6]
Remove the last item from the new list using pop:
[1, 2, 3, 4, 4]

=============================================================

Lists 5: List Transformations - Using filter() and map()

OPSs over 0.500: [0.981, 0.725, 0.891, 0.773, 0.7, 0.695, 0.788, 0.721, 0.895, 0.673, 0.601, 0.698, 0.742, 0.535, 0.53, 0.515, 0.535, 0.563]
The cubed root of the new list above is: [1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681996, 1.5874010519681996]
Cubing the new list above gives: [1, 8, 27, 64, 64]

=============================================================

Lists 6: List Transformations - Using List Comprehension

OPSs under 0.500: [0.492, 0.407, 0.302, 0.0]
OPSs tripled: [2.943, 2.175, 2.673, 2.319, 2.1, 2.085, 2.364, 2.163, 2.685, 2.019, 1.803, 2.094, 2.226, 1.605, 1.59, 1.545, 1.605, 1.476, 1.221, 1.689, 0.906, 0.0]
OPSs expressed as a percentage: [98.1, 72.5, 89.1, 77.3, 70.0, 69.5, 78.8, 72.1, 89.5, 67.3, 60.1, 69.8, 74.2, 53.5, 53.0, 51.5, 53.5, 49.2, 40.7, 56.3, 30.2, 0.0]

=============================================================

(base) kristenfinley@Kristens-MBP datafun-03-datatypes % 



"""
