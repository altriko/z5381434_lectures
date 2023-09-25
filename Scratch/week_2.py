# print('''John said: "Let's learn python together"''')
#
# a = 1.0
# b = float(1)
#
# print(type(b))
#
# 2==2
#
# print(str(5))
# str.upper("heho")

# length = 56
# width = 33
# height = 30.5
#
# volume = length * width * height
# print(volume)
#
#
# lst = [2, "string", True, None, True]
# print(f"Original lst is {lst}")
# lst.remove(True)
# print(f"Current lst is {lst}")


# email = "From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020"
# domain = email.split("@")[-1].split(" ")[0].upper()
# print(domain)


# After Python 3.6, order of insertion is preserved
dic = {1: 'first', 2: 'second', 3: 'third'}
# This will insert the 0 key at the end
dic[0] = 'fourth'
# This will NOT insert the key at the end because 1 exists
dic[1] = 'new first'
# Also, this does not return the first element of the dic
# because it was inserted at the end
print(dic)