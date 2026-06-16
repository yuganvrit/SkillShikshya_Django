# create a list and use reduce dunction to find products of all element in list

#To find the product of all elements in a list using reduce(),
# you first need to import it from functools
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# result = reduce(lambda x, y: x * y, numbers)

# print(result)


#there is a nested list constaining a list as a child using the reduce function flatten the list.
# [[1,2,3,4],[7,8,9],[7,6,1,2]]
# from functools import reduce

# nested_list = [[1,2,3,4],[7,8,9],[7,6,1,2]]

# result = reduce(lambda x, y: x + y, nested_list)

# print(result)

# create a list and use reduce dunction to find products of all element in list
# there is a nested list constaining a list as a child using the reduce function flatten the list.
# [[1,2,3,4],[7,8,9],[7,6,1,2]]


from functools import reduce

nested_list = [[1,2,3,4],[7,8,9],[7,6,1,2]]

# Flatten the list
flat_list = reduce(lambda x, y: x + y, nested_list)

print("Flattened list:", flat_list)

# Product of all elements
product = reduce(lambda x, y: x * y, flat_list)

print("Product:", product)