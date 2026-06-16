#unpacking tupple
# num = (1,2,3,4,5)
# a,b,c,d,e = num
# print(a)
# print(b)

# a, *b = num
# print(b)

#packing of tuple

# a = 1
# b = 2
# tupple = a, b
# print(tupple)

#classwork
#take input from user and create a tupple of 5 elements and print the tupple.

# a = input("Enter first number: ")
# b = input("Enter second number: ")
# c = input("Enter third number: ")
# d = input("Enter fourth number: ")
# e = input("Enter fifth number: ")

# a,b,c,d,e = input("Enter five elements: ")

# print(type(tupple))

# user_input = tupple(input("Enter 5 elements separated by spaces: "))
# print(type(user_input))

#take input from user single time only and take a numbers separated by comma and print every single element from input.

# user_input = input("Enter numbers separated by comma: ")
# print(type(user_input))
# a, b, c, d, e = user_input
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#nested tupple

# nested_tupple = (1, 2, (3, 4), 5)
# print(nested_tupple[2][1])

# #mutable data type in python

# mutable_tupple = (1,2,[3,4],5)
# print(type(mutable_tupple))
# mutable_tupple(2).append(7)
# print(mutable_tupple)


mutable_tupple = (1,2,'santos',5)
mutable_tupple = (1,2,'santosh',5)
print(mutable_tupple)

#another way
mutable_tupple = (1,2,'santos',5)
mutable_tupple = mutable_tupple[:2] + ('santosh',) + mutable_tupple[3:]
print(mutable_tupple)

#another way
mutable_tupple = (1,2,'santos',5)   
mutable_tupple = list(mutable_tupple)  # convert to list
mutable_tupple[2] = 'santosh'          # modify the list
mutable_tupple = tuple(mutable_tupple)  # convert back to tuple
print(mutable_tupple)   

#another trick
mutable_tupple = (1,2,'santos',5)  
mutable_tupple = (*mutable_tupple[:2], 'santosh', *mutable_tupple[3:])  # unpack and repack
print(mutable_tupple)

#again
mutable_tupple = (1,2,'santos',5)
mutable_tupple = (mutable_tupple[0], mutable_tupple[1], 'santosh', mutable_tupple[3])  # create new tuple with modified value
print(mutable_tupple)

#create a example nested tupple with 3 level depth

three_level_tupple = (1, (2, (3, 4)), 5)
print(three_level_tupple[1][1][0])  # Accessing the value 3







