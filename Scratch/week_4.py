# #Scratch for W4
# def qan_tic():            # (1)
#     tic = "QAN.AX"        # (2)
#     # print(tic)            # (3)
#     return tic            # (4)
#
# # res = qan_tic()
# # print(res)
# tic = "WES.AX"
# print(tic)
# print(qan_tic())

'''
TLDR:
If no `return` parameter -> it will return `None` -> as a Nonetype()
After `return`, nothing will be processed (that's why return is always at the end)
'''


#print even numbers from given lists, and return those

# list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
# def even_check(lis):
#     # lis_2 = []
#     # for i in lis:
#     #     if i % 2 == 0:
#     #        lis_2.append(i)
#     #        # print(_list_2)
#     #     else:
#     #         pass
#     # return print(_list_2)
#     return [i for i in lis if i % 2 == 0]
#
# print(even_check(list))


#Comprehension Dictionary
#
# pairs = [
#   ('a', 1),
#   ('b', 2),
#   ('c', 3),
#   ]
#
# # x = {}
# # x.update({i:j}) for i, j in pairs
# # print(x)
#
#
# dic = {}                                              # (1)
#
# # Iterate over each tuple in `pairs` and update the dictionary
# dic.update({key:value}) for key, value in pairs       # (2 + 3)
#
# pairs = [
#     ('a', 1),
#     ('b', 2),
#     ('c', 3),
# ]
# # Create an empty dictionary
# dic = {}  # (1)
#
# # Iterate over each tuple in `pairs` and update the dictionary
# dic.update({key: value}) for key, value in pairs  # (2 + 3)


#
# lst = [2,3,10,14,20,21,25,13,15]
# x = [i**2 for i in lst if i**2 > 150]
# print(x)

numbers = [0,1,1,2,5,6,8,2,4,6,8]
#unique integers exist in numbers and divsible by 2

x = list({i for i in numbers if i % 2 == 0})
print(x)