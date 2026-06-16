# map filter and reduce  are higher order functions

# map function takes a function and an iterable and 
# applies the function to each element of the 

# creates a function that takes a list of string and 
# returns a list of the length of each string using map function
# for example if the input is ["hello", "world"] the output should be [5,5]


def length_of_strings(words):
    return list(map(len, words))

result = ["hello", "world"]
print(length_of_strings(result))

def filter_even_numbers(x):
    return x % 2 == 0

numbers = [1,2,3,4,5,6]
print(list(filter(filter_even_numbers, numbers)))






# create a function that takes a list of string and
# returns a list of strings that have length greater than 5 using filter function
# for example if the input is ["hello", "world", "python"] the output should be ["python"]


# by using lambda
def length_of_string(words):
    return list(filter(lambda word: len(word) > 5, words))

words = ["hello", "world", "python"]

print(length_of_string(words))


# without using lambda
def check_length(word):
    return len(word) > 5

def long_strings(words):
    return list(filter(check_length, words))

words = ["hello", "world", "python"]
print(long_strings(words))


