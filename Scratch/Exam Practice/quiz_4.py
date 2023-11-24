'''Quiz 4.py'''
# ------------------------
# Slide 1
# ------------------------
'''Define a function process_string(s) with the following characteristics:
    - It accepts a string s as a parameter
    - I returns a list with the following characteristics:
        -The string s is split into a list of words (we define words as
        sequences of alphanumeric characters separated by white spaces).
        - All of the words in the list are in lower case

When testing functions, you may add diagnostic code to your Python file and examine the
output using the Run button. For example, you may wish to add a line like
print(process_string("This is my test String")) which should return a
list ['this', 'is', 'my', 'test', 'string']. 

However, the Mark button will test your function with random sentences
(with meaningless "words"). This ensures the function works as desired. 

'''
# def funct(s):
#     return list(s.lower().split())
#
# if __name__ == "__main__":
#     a = "this is my test string"
#     print(funct(a))

# ------------------------
# Slide 2
# ------------------------
'''Define a function process_string(s) with the following characteristics:
    - It accepts a string s as a parameter
    - I returns a list with the following characteristics:
        - The string s is split into a list of words.
        - If the word is in a position with an even index, it is returned in lower case. 
        - If the word is in a position with an odd index, it is returned in upper case

    Note that:
    - You can test if x is even using the expression x % 2 == 0, which will return
    True if x is even and False otherwise.
    - 0 is an even number

    When testing functions, you may add diagnostic code to your Python file and
    examine the output using the Run button. For example, you may wish to add a line
    like print(process_string("This is my test String")) which should return a
    list ['this', 'IS', 'my', 'TEST', 'string']. 

    However, the Mark button will test your function with random sentences.
    This ensures the function works as desired. 

'''
# def funct(s):
#     x = []
#     for i, j in enumerate(s.split()):
#         if i % 2 == 0:
#             x.append(j.lower())
#         else:
#             x.append(j.upper())
#     return x
#
# print(funct("This is my test string"))

# ------------------------
# Slide 3
# ------------------------
'''Write a function called fizz_buzz_sumz(i) which takes a positive integer i > 0 and
returns the sum of a sequence of numbers constructed as follows:
    - Start the sum at 0
    - For each integer x from 1 through (and including) i:
        - If the integer x is divisible by 3 but not 5,
        add the value 3 * x (that is, "x times 3")
        - If the integer x is divisible by 5 but not 3,
        add the value of 5 * x (that is, "x times 5")
        - If the integer x is divisible by 3 and divisible by 5,
        ignore the integer (so do not add any value to the sum).
        - Otherwise, add the actual value of x to the sum
        
    For example, if i=10 , the sum above should be 151, which is computed
    as 1 + 2 + 3*3 + 4 + 5*5 + 6*3 + 7 + 8 + 9*3+ 10*5.

'''
# def fizz_buzz_sumz(i):
#     sum = 0
#     for j in range(i+1):
#         if j % 3 == 0 and j % 5 != 0:
#             sum += 3 * j
#         elif j % 3 != 0 and j % 5 == 0:
#             sum += 5 * j
#         elif j % 3 == 0 and j % 5 == 0:
#             pass
#         else:
#             sum += j
#     return sum
#
# print(fizz_buzz_sumz(10))


# ------------------------
# Slide Comprehensions
# ------------------------
'''
Given this dictionary:
1. Define a variable sorted_keys that will contains the keys of prc_dic in
ascending order. Use a list comprehension to do this in a single line
The following references might help:
    - list.sort method :   https://docs.python.org/3/library/stdtypes.html#list.sort
    - sorted builtin   :   https://docs.python.org/3/library/functions.html#sorted
2. Replace the prc_dic key for 3000-01-15 with 2020-01-15. Do this in one line
and without explicitly writing the value 7.0400.

'''
# prc_dic = {
#     '3000-01-15': 7.0400,
#     '2020-01-14': 7.1100,
#     '2020-01-13': 7.0200,
#     '2020-01-02': 7.1600,
#     '2020-01-03': 7.1900,
#     '2020-01-06': 7.0000,
#     '2020-01-07': 7.1000,
#     '2020-01-08': 6.8600,
#     '2020-01-09': 6.9500,
#     '2020-01-10': 7.0000,
# }
#
# #1
# sorted_keys = sorted([i for i, j in prc_dic.items()])
# print(sorted_keys)
#
# #2
# prc_dic['2020-01-15'] = prc_dic.pop('3000-01-15')
# print(prc_dic)

# ------------------------
# Slide Text, unicode, bytes
# ------------------------

'''
The copyright symbol is: ©
The copyright symbol has Unicode hex value: \u00A9

- You should not use the Unicode literal © inside your solution.
Make sure that you use the hex value 00A9. 
- There should be no white spaces (or empty lines)
before or after each print statement.
This means that the first character printed should be `The`.

'''
print("The copyright symbol is: \u00A9")
print("The copyright symbol has Unicode hex value: \\u00A9")