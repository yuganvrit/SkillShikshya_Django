# tup = (1,2,3,4,5)

# print(tup[0])

# print(tup)
# leng= len(tup)
# print(tup[0:leng:leng-1])


# tupple = (1,2,3)

# a, b,c = tupple

# print(a, b, c)

# packing a tupple

# tupple = a, b
# print(tupple)

# take input fro muser and create a tupple of 5 elements and print the tupple

# a = input("Enter first element")
# b = input("Enter second element")
# c = input("Enter third element")
# d = input("Enter forth element")
# e = input("Enter fifth element")

# tupple = tuple(input("Enther five elements: "))
# print(tupple)
# print(type(tupple))


#take input from user single time only and take a numbers separated by comma and print every single elements from input.

# a,b,c,d,e = input("Enther five elements: ")


# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# #nested tupple
# nested_tupple = (1,2,(3,4))
# print(nested_tupple[2][1])

# mutable data type in tuple 
mutable_tuple = (1,2,[3,4])
print(mutable_tuple)

mutable_tuple[2].append(5) # (1,2,[3,4,5])   tuple with new list.
print(mutable_tuple) # (1,2,[3,4,5])

mutable_tuple = (1,2,'Santos', 5)
mutable_tuple = (1,2,mutable_tuple[2]+"h", 5, 'Santos') 

print(mutable_tuple)
