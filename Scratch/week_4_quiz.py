#quiz 1
# def process_string(s):
#     return s.lower().split()
#
# print(process_string("This is my test String"))



# #Quiz 2
# def process_string(s):
#     x = s.split()
#     y = []
#     for i in x:
#         if x.index(i) % 2 == 0:
#             y.append(i.lower())
#         else:
#             y.append(i.upper())
#     return y
#
# print(process_string("This is my test String"))
#


# #Quiz 3
# def fizz_buzz_sumz(i):
#     if i > 0:
#         y = 0
#         for x in range (1, i+1):
#             if x % 3 == 0 and x % 5 != 0:
#                 y += 3 * x
#             elif x % 3 != 0 and x % 5 == 0:
#                 y += 5 * x
#             elif x % 3 == 0 and x % 5 == 0:
#                 pass
#             else:
#                 y += x
#             print (f'sequence:{x} sum: {y}')
#         return y
#     else:
#         pass
#
# print(fizz_buzz_sumz(10))

#Quiz 4
prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
#1
sorted_keys = sorted([i for i, j in prc_dic.items()])
print(sorted_keys)

#2
# prc_dic.keys() = "2020-01-15"
# sorted_keys[(len(sorted_keys)-1)] = "2020-01-15"
# print(sorted_keys)

prc_dic['2020-01-15'] = prc_dic.pop('3000-01-15')
print(prc_dic)