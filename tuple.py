# tup = (2, 3, 4, 5, 6)
# print(id(tup))
# tup = (1, 2, 3, 4, 5)
# print(id(tup))

# tup.pop()
# print(tup)

# tup = 1, 2, 3, 4, 5 ---> Tuple nai hunxaaa!!

# print(tup[2])
# length = len(tup)
# print(tup[0:length:length-1])

#Unpacking Tuple
# a, b, *c = tup
# print(a)
# print(b)
# print(c)

#Packing Tuple
# a = 6
# b = 7
# c = 8
# tupple = a, b, c
# print(tupple)

#Task: Take input from user and create a tuple of 5 elements and print the tupple

# a = input("Enter a number: ")
# b = input("Enter a number: ")
# c = input("Enter a number: ")
# d = input("Enter a number: ")
# e = input("Enter a number: ")

# tuplee = a, b, c ,d, e
# print(tuplee)
# print(type(tuplee))

#2nd method:
# user_inputs = tuple(input("Enter 5 Different numbers: "))
# print(user_inputs)

#Task2: Take input from user single time only and take a numbers separated by comma and print every single element from input
# user_inputs = tuple(input("Enter 5 Different numbers: "))
# print(user_inputs)
# a, b, c, d, e = user_inputs
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#Tuple have only 2 methods: Count() and Index().

#Nested Tuple
# nested_tup = (1, 2, (3, 4), 5)
# print(nested_tup[2][1])

# #mutable datatype in tuple
# mutable_tup = (1, 2, [3, 4], 5)
# mutable_tup[2].append(9)
# print(mutable_tup)

# # mut_tup = (1, 2, 'Santos', 4)
# # mut_tup[2] = 'Santosh'
# # print(mut_tup)  homeworkkkkkkk!!!!

# three_lvl_tup = (1, (2, (3, 4)), 5)
# print(three_lvl_tup[1][1][1])

#Range datatype

#Range is an only datatype which is a function by itself!

first_five_numbers = range(6)
print(id(first_five_numbers))
print(first_five_numbers)
print(type(first_five_numbers))

first_five_numbers = range(7)
print(id(first_five_numbers))

four = range(4, 41, 2)
print(list(four[::2]))

eight = range(8, 81, 4)
print(list(eight[::2]))