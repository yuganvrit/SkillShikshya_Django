#filter() is a built-in function used to select only those elements from an iterable (like list, tuple, etc.) that satisfy a condition.
# syntax:
# filter(function, iterable)

# filter → a condition (returns True or False)
# iterable → list, tuple, etc.
# It returns a filter object, so we usually convert it into a list using list().


numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# for odd 

numbers = [1, 2, 3, 4, 5, 6]

odd = list(filter(lambda x: x % 2 != 0, numbers))

print(odd)


