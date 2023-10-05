##Quiz 3
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
# # print(f_suburbs)
#
# for i in f_suburbs:
#     if i[:6] != "Forest" and f_suburbs[i] is not None:
#         print(f"{i}: {f_suburbs[i]}")
#     else:
#         pass


##Quiz 4
# Look over all integers from 1 to 100, doing the following:
# - If the integer is divisible by 3 (but not by 5), write its value and Fizz. e.g., 12: Fizz
# - If the integer is divisible by 5 (but not by 3), write its value and Buzz, e.g., 25: Buzz
# - If the integer is divisible by 3 and divisible by 5, write its value and FIZZ BUZZ (in caps), e.g. 15: FIZZ BUZZ
# - If none of the above apply, simply print the integer value
#
# To check if an integer j is divisible by 3, for example, use the logical expression j % 3 == 0.


def checker(numeric):
    if numeric % 3 == 0 and numeric % 5 != 0:
        print(f"{numeric}: Fizz")
    elif numeric % 3 != 0 and numeric % 5 == 0:
        print(f"{numeric}: Buzz")
    elif numeric % 3 == 0 and numeric % 5 == 0:
        print(f"{numeric}: FIZZ BUZZ")
    else:
        print(numeric)

for i in range(1,101):
    checker(i)


#Quiz 5
# Using the provided list l, loop over the elements and print their positional index and value. The print format should be POSITIONAL_INDEX: SUBURB. So, Fairfield would look like:
# 0: Fairfield

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

# for i in l:
#     print(f"{l.index(i)}: {i}")



# ##Quiz 6
# first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
# middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
# last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']
#
# for last in last_names:
#     for first in first_names:
#         for middle in middle_names:
#             if middle is not None:
#                 print(first, middle, last)
#             else:
#                 print(first, last)

