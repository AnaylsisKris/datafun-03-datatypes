"""
Task 5 Output 
Create a new empty file user_tuples_etc_out.py to hold your output. 
Copy and paste your terminal output after a run.
Communicate clearly for maximum credit.



/usr/local/bin/python3 /Users/kristenfinley/Documents/datafun-03-datatypes/user_tuples_etc.py
(base) kristenfinley@Kristens-MBP datafun-03-datatypes % /usr/local/bin/python3 /Users/kristenfinley/Documents/datafun-03-datatypes/user_tuples_etc.py


TUPLES .......................................................
==============================================================
4. Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.


Starters = ('Paul Goldschmidt', 'Tommy Edman', 'Nolan Arenado', 'Brendan Donovan', "Tyler O'Neill", 'Dylan Carlson', 'Lars Nootbaar', 'Albert Pujols', 'Andrew Knizner')

Backup = ('Nolan Gorman', 'Harrison Bader', 'Corey Dickerson', 'Juan Yepez', 'Yadier Molina', 'Paul DeJong', 'Edmundo Sosa')

Roster = ('Paul Goldschmidt', 'Tommy Edman', 'Nolan Arenado', 'Brendan Donovan', "Tyler O'Neill", 'Dylan Carlson', 'Lars Nootbaar', 'Albert Pujols', 'Andrew Knizner', 'Nolan Gorman', 'Harrison Bader', 'Corey Dickerson', 'Juan Yepez', 'Yadier Molina', 'Paul DeJong', 'Edmundo Sosa')

Were 2022's two most beloved Cardinals Starters?
Pujols is a starter? True
Molina is a starter? False

There are 16 players on the roster.
However, only 9 players can be in the starting line up.
Roster[0]= 'Paul Goldschmidt' is ranked first, so he will definitely make the cut.
How many players on the roster must play bench warmer per game?
Quotient: 1, Remainder of 7 benchwarmers


SETS .......................................................    
==============================================================
5. Sets: create two sets. Get the intersection and the union.


Converting the roster position tuple to a set can give the starting positions by removing duplicates:
{'C', 'DH', '3B', 'LF', 'CF', 'SS', '1B', '2B', 'RF', 'OF'}

The set of starting positions can be joined with the set of pitching positions with a union:
{'C', 'DH', 'Releaver', 'Closer', '3B', 'LF', 'CF', 'SS', '1B', '2B', 'Starter Pitcher', 'RF', 'OF'}

The set of starting positions can be joined with the set of back up positions using set intersection to remove duplicates:
{'C', 'LF', 'CF', 'SS', '2B', 'OF'}

The duplicates can be determined by difference:
{'3B', 'DH', 'RF', '1B'}


DICTIONARIES .......................................................    
==============================================================
7. Use a dictionary to create key-value pairs of each word and its count from a file.


{'Beautiful': 1, 'is': 10, 'better': 8, 'than': 8, 'ugly.': 1, 'Explicit': 1, 'implicit.': 1, 'Simple': 1, 'complex.': 1, 'Complex': 1, 'complicated.': 1, 'Flat': 1, 'nested.': 1, 'Sparse': 1, 'dense.': 1, 'Readability': 1, 'counts.': 1, 'Special': 1, 'cases': 1, "aren't": 1, 'special': 1, 'enough': 1, 'to': 5, 'break': 1, 'the': 5, 'rules.': 1, 'Although': 3, 'practicality': 1, 'beats': 1, 'purity.': 1, 'Errors': 1, 'should': 2, 'never': 2, 'pass': 1, 'silently.': 1, 'Unless': 1, 'explicitly': 1, 'silenced.': 1, 'In': 1, 'face': 1, 'of': 2, 'ambiguity,': 1, 'refuse': 1, 'temptation': 1, 'guess.': 1, 'There': 1, 'be': 3, 'one--': 1, 'and': 1, 'preferably': 1, 'only': 1, 'one': 2, '--obvious': 1, 'way': 2, 'do': 2, 'it.': 1, 'that': 1, 'may': 2, 'not': 1, 'obvious': 1, 'at': 1, 'first': 1, 'unless': 1, "you're": 1, 'Dutch.': 1, 'Now': 1, 'never.': 1, 'often': 1, '*right*': 1, 'now.': 1, 'If': 2, 'implementation': 2, 'hard': 1, 'explain,': 2, "it's": 1, 'a': 2, 'bad': 1, 'idea.': 2, 'easy': 1, 'it': 1, 'good': 1, 'Namespaces': 1, 'are': 1, 'honking': 1, 'great': 1, 'idea': 1, '--': 1, "let's": 1, 'more': 1, 'those!': 1}



(base) kristenfinley@Kristens-MBP datafun-03-datatypes % 


"""