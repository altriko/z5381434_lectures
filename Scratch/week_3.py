# evens = []
# for i in range(1_000_000 + 1):
#     if i % 2 == 0:
#         evens.append(i)
#
# print(evens[:10])
#
#
# evens_2 = [x for x in range(1_000_000 + 1) if x % 2 == 0]
# print(evens_2[:10])

# name = input("Who are you?")
# print("Welcome to the class,", name)


# ot_rate = 51.45
# normal_rate = 89.9
# threshold = 35
#
# def pay_calc(hr):
#     if hr > threshold:
#         return (ot_rate * (hr - threshold)) + normal_rate * threshold
#     else:
#         return normal_rate * hr
#
# calc = int(input("Number of hours you work: "))
# result = pay_calc(calc)
# print("Your rate is:", result)

# numbers = [3, 9, 1, 5, 7, 2, 15, 0, 3, 12, 3, 15, 3]
#
# x = numbers[0]
# for i in numbers:
#     if i > x:
#         x = i
#     else:
#         pass
# print(x)
# print(max(numbers))

# for i in range(1,4):
#     for j in range (1,4):
#         if j >= i:
#             print(i, j)



# sum_of_evens = 0
# for i in range(1,101):
#     print(f'Loop is on {i}')
#     if i % 2 == 1:      # i is odd
#         continue
#     print(f'    summing the value of {i}')
#     sum_of_evens = sum_of_evens + i
# print(f'Sum of evens is {sum_of_evens}')


for even in range(0, 10, 2):
    if even > 2:
        break

    print(even)
