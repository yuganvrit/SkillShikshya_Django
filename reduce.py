# reduce() is used to apply a function repeatedly on a sequence to reduce it to a single value.
# reduce() is not a built-in function anymore in Python 3, so you must import it:
# from functools import reduce
# syntax: reduce(function, iterable)
# function → takes 2 arguments
# iterable → list, tuple, etc.
# returns a single value

# addition of all numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)

# find maxM

from functools import reduce

numbers = [10, 5, 25, 3, 18]

maximum = reduce(lambda x, y: x if x > y else y, numbers)

print(maximum)

# 🔹 Difference from map/filter
# map() → transforms each element
# filter() → selects elements
# reduce() → combines everything into one value