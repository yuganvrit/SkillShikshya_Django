# # A lambda function in Python is a small anonymous function (a function without a name) used for short, simple operations.
# # lambda arguments: expression
# # add = lambda a, b: a + b

# # print(add(2, 3))


# # numbers = [1, 2, 3, 4, 5]

# # result = list(map(lambda x: x ** 3, numbers))

# # print(result)

# wrong code
# list = ['s', 'a', 'm', 'i', 'r']

# result = reduce(lambda x:y:x+y,list)

# print(result)

from functools import reduce

lst = ['s', 'a', 'm', 'i', 'r']

result = reduce(lambda x, y: x + y, lst)

print(result)

# # find the string with largest length from list using builtin hugherorder functions and lambda func. as argument


# # words = ["samir", "django", "banana", "kiwi", "watermelon",]

# # result = max(words, key=lambda x: len(x))

# # print(result)

# # multiple of elements
# # numbers = [1, 2, 3, 4, 5]

# # result = list(map(lambda x: x ** 3, numbers))
# # print(result)

# # convert a list of strings into integers

# # numbers = ['10', '20', '30', '40',]
# # # result = list(map(lambda x: int(x), numbers))

# # result = list(map(int, numbers)) # becz int itself is a function, so wee don't need lambda
# # print(result)

# # adding 10 to every numbers

# numbers = [5,10,15,20]
# result = list(map(lambda x : x+10, numbers))
# print(result)

# # calculating the length of each string

# string = ['samir', 'ram', 'shyam', 'watermelon']
# result = list(map(lambda x : len(x), string))
# print(result)

# # Multiply corresponding elements of two lists

# a = [1, 2, 3]
# b = [4, 5, 6]

# result = list(map(lambda x,y : x*y, a,b ))
# print(result)

# # Extract the first character of each string
# string = ["Samir", "Python", "Django"]
# result = list(map(lambda x : x[0], string))
# print(result)

# # Convert temperatures from Celsius to Fahrenheit
# # f = 9/5*c+32

# celsius = [0, 10, 20, 30]

# fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))

# print(fahrenheit)

# # Convert a list of tuples into full names

# names = [
#     ("Samir", "Chaudhary"),
#     ("Ram", "Sharma"),
#     ("Hari", "Thapa")
# ]

# result = list(map(lambda x: x[0] + " " + x[1], names)) # tuple → lambda processes → string → map collects → list()
# print(result)

# # extract only names
# data = [
#     {"name": "Samir", "age": 20},
#     {"name": "Ram", "age": 25},
#     {"name": "Hari", "age": 22}
# ]

# names = list(map(lambda x: x["name"], data))

# print(names)

# # extract both name and age

# data = [
#     {"name": "Samir", "age": 20},
#     {"name": "Ram", "age": 25},
#     {"name": "Hari", "age": 22}
# ]

# names = list(map(lambda x: (x["name"] , x['age']), data))

# print(names)

# sorted no. in descending order

nums = [5, 2, 9, 1, 7]
result = sorted(nums, key=lambda x: -x)
print(result)
# [9, 7, 5, 2, 1]

# sorting strings by length

words = ["apple", "kiwi", "banana", "fig"]
result = sorted(words, key=lambda x: len(x))
print(result)
# ['fig', 'kiwi', 'apple', 'banana']

#srting a list of dict. by one key

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 35},
]

result = sorted(people, key=lambda x: x["age"])
print(result)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Carol', 'age': 35}]

# sorting tuple by second element
pairs = [("a", 3), ("b", 1), ("c", 2)]
result = sorted(pairs, key=lambda x: x[1])
print(result)
# [('b', 1), ('c', 2), ('a', 3)]

# sorting by multiple criteria (e.g., role, then name)
people = [
    {"name": "Bob", "role": "editor"},
    {"name": "Alice", "role": "admin"},
    {"name": "Carol", "role": "admin"},
]

result = sorted(people, key=lambda x: (x["role"], x["name"]))
print(result)
# [{'name': 'Alice', 'role': 'admin'}, {'name': 'Carol', 'role': 'admin'}, {'name': 'Bob', 'role': 'editor'}]

#Reverse sorting with reverse=True

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
]

result = sorted(people, key=lambda x: x["age"], reverse=True)
print(result)
# [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]