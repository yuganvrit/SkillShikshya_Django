# value = lambda x: x * 2

# print(value(5))


# #classwork

# #create a map function that returns cubes of a number using lambda function as an argument

# number=[1,2,3,4,5]
# cubes = list(map(lambda x: x*3, number))
# print(cubes)


# #use lambda function reduce to find max number
from functools import reduce

# maximum = reduce(lambda x, y: x if x>y else y, number)
# print(maximum)

lst = ['s','a','n','t','o','s','h']

string = reduce(lambda x, y: x+y, lst)
print(string)

words = ['e','l','e','p','h','a','n','t']
vowels = list(filter(lambda x:x in 'aeiou', words))
print(vowels)

list = [1,2,3,4,5]
maximum = reduce(lambda x, y: x if x>y else y, list)
print(maximum)


#c/w

#find the string with largest length from list using builtin highorder function and lambda function as argument

strlst = ['santosh', 'ram', 'hari', 'shyam', 'elephant']

maxstr = reduce(lambda x,y: x if len(x) > len(y) else y, strlst)
print(maxstr)