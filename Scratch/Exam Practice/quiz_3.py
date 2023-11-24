'''Week 3'''
# ------------------------
# Slide 1
# ------------------------

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for i in l:
#     print(i)

# ------------------------
# Slide 2
# ------------------------
'''Using the provided list l, loop over the elements. However, only print them if
they do not begin with the letters "Forest". Use an if statement.
You may extract letters from a string using a slice.
'''

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for i in l:
#     if i[:6] != "Forest":
#         print(i)

# ------------------------
# Slide 3
# ------------------------
'''Using the Dictionary provided, print out the town and population for each of the suburbs beginning with f meeting the following criteria:
- The suburb's name does not begin with "Forest"
- The population data exists. This means that the population is not None. In fact, is not None is how you test for that a value is not None in Python. Smart!
Each line in the output should look like SUBURB_NAME: POPULATION.

So, for example, Fairfield would be:
Fairfield: 18081
'''

# f_suburbs = dict()
# f_suburbs["Fairfield"] = 18081
# f_suburbs["Fairfield East"] = 5273
# f_suburbs["Fairfield Heights"] = 7517
# f_suburbs["Fairfield West"] = 11575
# f_suburbs["Fairlight"] = 5840
# f_suburbs["Fiddletown"] = 233
# f_suburbs["Five Dock"] = 9356
# f_suburbs["Flemington"] = None
# f_suburbs["Forest Glen"] = None
# f_suburbs["Forest Lodge"] = 4583
# f_suburbs["Forestville"] = 8329
# f_suburbs["Freemans Reach"] = 1973
# f_suburbs["Frenchs Forest"] = 13473
# f_suburbs["Freshwater"] = 8866
#
# for i in f_suburbs:
#     if f_suburbs[i] != None and i[:6] != "Forest":
#         print(f"{i}: {f_suburbs[i]}")

# or -- but it's not working :/
# for town, pop in f_suburbs:
#     if town[0:6] != "Forest" and pop is not None:
#         print(f'{town}: {pop}')

# ------------------------
# Slide 4
# ------------------------
'''Look over all integers from 1 to 100, doing the following:
- If the integer is divisible by 3 (but not by 5), write its value and Fizz. e.g., 12: Fizz
- If the integer is divisible by 5 (but not by 3), write its value and Buzz, e.g., 25: Buzz
- If the integer is divisible by 3 and divisible by 5, write its value and FIZZ BUZZ (in caps), e.g. 15: FIZZ BUZZ
- If none of the above apply, simply print the integer value

To check if an integer j is divisible by 3, for example, use the logical expression j % 3 == 0.
'''
# def integer_check(numeric):
#     if numeric % 3 == 0 and numeric % 5 != 0:
#         print(f"{numeric}: Fizz")
#     elif numeric % 5 == 0 and numeric % 3 != 0:
#         print(f"{numeric}: Buzz")
#     elif numeric % 3 == 0 and numeric % 5 == 0:
#         print(f"{numeric}: FIZZ BUZZ")
#     else:
#         print(numeric)
#
# for i in range(1,101):
#     integer_check(i)

# ------------------------
# Slide 5
# ------------------------
'''Using the provided list l, loop over the elements and print their positional index and value.
The print format should be POSITIONAL_INDEX: SUBURB. So, Fairfield would look like:

0: Fairfield '''

# l = ["Fairfield",
#     "Fairfield East",
#     "Fairfield Heights",
#     "Fairfield West",
#     "Fairlight",
#     "Fiddletown",
#     "Five Dock",
#     "Flemington",
#     "Forest Glen",
#     "Forest Lodge",
#     "Forestville",
#     "Freemans Reach",
#     "Frenchs Forest",
#     "Freshwater"]
#
# for i in l:
#     print(f"{l.index(i)}: {i}")
#
# for i, name in enumerate(l):
#     print(f"{i}: {name}")

# ------------------------
# Slide 6
# ------------------------
'''It turns out that your friend's name, 'Joseph Johnathan Smith'
isn't flashy enough for Hollywood. You have decided to help them by
making a list of all combinations of the top 5 male movie stars in 2020:

1. Dwayne "The Rock" Johnson
2. Ryan Rodney Reynolds
3. Mark Robert Michael Wahlberg
4. Ben Geza Affleck
5. Vin Diesel

Using the provided first_names, middle_names, and last_names list, print out
all possible combinations.
Names should read their natural order: first middle last. 

Loop over all possible combinations for a last name first.
So, do all the "Johnson" names. Then, loop over all possible
combinations of first names, followed by combinations of
middle names. Note that None means that there is no middle name
and not that the middle name is "None".

This means the first few names in your list should be:

Dwayne "The Rock" Johnson 
Dwayne Rodney Johnson 
Dwayne Robert Michael Johnson 
Dwayne Geza Johnson
Dwayne Johnson
Ryan "The Rock" Johnson
Ryan Rodney Johnson

Spacing matters, so make sure you don't have two spaces when the
middle name is not present.
'''

# first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
# middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
# last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
#
# for i in first_names:
#     for j in middle_names:
#         for k in last_names:
#             if j != None:
#                 print (i,j,k)
#             else:
#                 print (i,k)