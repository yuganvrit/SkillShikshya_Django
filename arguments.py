# positional arguments

# def add(a, b):
#     return a + b
# print(add(10,20))

# create a function that takes 5 poitional arguments
# check if the number is even or odd and return the sum of even numbers.
# and the sum of odd number separately.

# def check_numbers(a,b,c,d,e):
#     numbers = [a,b,c,d,e]
#     even_sum = 0
#     odd_sum = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num

#     return even_sum, odd_sum


# nums = (1,2,3,4,5)

# even, odd = check_numbers()
# print("Even sum:", even)
# print("Odd sum:", odd)

# if we assign variable in function then it does not care about list,tuple or anything(mutable or immutable) it only cares whether it is iterable or not.
# def check_numbers(numbers):
#     even_sum = 0
#     odd_sum = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num

#     return even_sum, odd_sum

# nums = [1,2,3,4,5]   # list OR tuple both work

# even, odd = check_numbers(nums)

# print("Even sum:", even)
# print("Odd sum:", odd)

# def sum_natural_numbers(*args):
#     sum = 0 # keeping outside the loop sum = 0 gives you 15 output
#     for element in args:
#         sum += element
#     return sum



# result = sum_natural_numbers(1,2,3,4,5)
# print(result)    

# # create a function that 
# #takes any number of arguments
# # return maximum and minimum number from the arguments passed


def find_min_max(*args):
    return max(args), min(args)

maximum, minimum = find_min_max(1,2,10,20,30,100)

print("Maximum:", maximum)
print("Minimum:", minimum)

# creates a function that takes a list
# and return a dict with length, max, min, sum and average
# key value pairs


# def list_stats(lst):
#     if not lst:
#         return {"length": 0, "max": None, "min": None, "sum": 0, "average": None}
    
#     return {
#         "length": len(lst),
#         "max": max(lst),
#         "min": min(lst),
#         "sum": sum(lst),
#         "average": sum(lst) / len(lst)
#     }
# my_list = [10, 20, 30, 40, 50]
# result = list_stats(my_list)
# print(result)


def sum_natural_numbers(*args):
    sum = 0 # keeping outside the loop sum = 0 gives you 15 output
    for element in args:
        sum += element
        return sum
result = sum_natural_numbers(1,2,3,4,5)
print(result)    






















