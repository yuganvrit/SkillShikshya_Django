## Task 
# import random

# #generate random integer with in range
# number = random.randint(1,10)
# print(number)

# import random

# def play_game():
#     secret_number = random.randint(1, 100)
#     counter = 0
#     guess_list = []

#     while counter < 7:
#         user_input = int(input("Enter a number: "))

#         if user_input > secret_number:
#             guess_list.append(user_input)
#             print("Too high")
#             counter += 1

#         elif user_input < secret_number:
#             guess_list.append(user_input)
#             print("Too low")
#             counter += 1

#         else:
#             guess_list.append(user_input)
#             print(f"You guessed the correct number: {user_input}")
#             break

#     return guess_list

# print(play_game())


## buit in higher order function

# reduce() this is built in higher order function
#reduce le jahile single value return garthyo

# from functools import reduce
# def total_sum(x,y):
#     return x + y

# list = [1,2,3,4,5]
# sum = reduce(total_sum, list)
# print(sum)


##classwork 
#create a list and use reduce functions to find the product of all elements in list
# from functools import reduce
# list = [1,2,3,4,5]
# def total_product(a,b):
#     return a * b

# product = reduce(total_product, list)
# print(product)


#there is a nested list contain in a list as a child using the reduce function flatten the list

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
# flat_list = []
# def flatten_list(nested_list):

#     for sublist in nested_list:
#         for item in sublist:
#             flat_list.append(item)

#     return flat_list
# result = flatten_list(numbers)
# print(result)

##Lambda functions
# lambda arguments : expression
# value = lambda x : x*2

# print(value(2))



# ## Classwork
# #create a map function that return cubes of numbers using lambda function as a argument

# from functools import reduce

# # numbers = [1, 2, 3, 4]
# # # cube = list(map(lambda x: x ** 3, numbers))
# # # print(cube)  

# # max = list(reduce(lambda x : max(), numbers))
# # print(max)


# list = ['p','r','i','n','c','e']

# result = reduce(lambda a,b: a+b, list)
# print(result)


## tenary expression in lambda functions
# from functools import reduce
# list = [1,2,3,4,5]
# result = reduce(lambda x,y : x if x > y else y , list)
# print(result)


##classwork
# find the string with largest kength from list using built in higher order functions and lambda function as argument

# list =['ram', 'prince', 'alice']
# result = reduce(lambda x,y: x if len(x) > len(y) else y,list)
# print(result)






