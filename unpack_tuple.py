#unpacked tupple

# tupple = (1, 2, 3, 4, 5)
# a, b, c, d, e = tupple
# print(a)
# print(b)
# print(c)

# a, *b = tupple
# print(b)

# a, *b, c = tupple
# print(b)

#taking input from user and creating a tupple of 5 elements and printing the tupple.
# a = input("Enter first number: ")
# b = input("Enter second number: ")    
# c = input("Enter third number: ")
# d = input("Enter fourth number: ")
# e = input("Enter fifth number: ")
# tupple = (a, b, c, d, e)
# print(tupple) 

#take input from user single time only and take a numbers separated by comma and print every single element from input.
# input_str = input("Enter 5 numbers separated by comma: ")
# numbers = input_str.split(",")
# a, b, c, d, e = numbers
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#next tupple
next_tuple = (1,2,3,4,5,5,6,1,7,8,9,0)
next_tuple.count(0)
print(next_tuple.index(0))
print(next_tuple.index(5))

next_tuple.reverse(2)#gives error because tuple is immutable
print(next_tuple)
