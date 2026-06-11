# #positional arguments

# def add(a, b):
#    return a+b

# add(10, 30) #positional argument


# #classwork

# #create a function that takes 5 positional argyments and returns the sum of all the arguments.
# #check if the number is od or even. and return the sum of even numbers and the sum of odd numbers separately

# def check_and_sum(a,b,c,d,e):
#     odd = 0 
#     even = 0

#     new_value = [a,b,c,d,e]

#     for i in new_value:
#         if i%2 == 0:
#             even +=i
#         else:
#             odd +=i

#     return odd, even

 
# odd, even = check_and_sum(1,2,3,4,5)

# print(odd,even)


# #global keyword

# counter = 0

# def increment():
#     global counter
#     counter +=1
#     return counter

# increment()


# # *args 

# def sums(*args):
#     addition = 0
#     for i in args:
#         addition += i

#     print( addition)
# sums(1,2,3,4,5)
# sums(1,2,3,4)
# sums(1,2,3,4,5,5,3,2,1)



# # **kwargs

# def build_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} => {value}')

# build_profile(name = 'santosh', age =12, address = 'tokha')

#classword

#createa function taht takes any number of args return max and min number from the arguments passed.

def max_and_min(*args):
    return max(args), min(args)


print(max_and_min(1,2,3,4,5,6,7,8,9,23,23,353,12))

# #c/w

#creat a function that takes a list as argument and return  a dictionary with length, max, min, sum, and average key value pairs.

def ret_dict(lst):
    sumlst = sum(lst)
    length = len(lst)
    maximum = max(lst)
    minimum = min(lst)
    avg = sumlst/length

    return {'length': length, 'max': maximum, 'minimum':minimum, 'sum':sumlst, 'average': avg}

print(ret_dict([1,2,3,4,5,6,7]))


# kwargs
#write merge_profiles(**users) that takes keyword arguments like alice =25, bob=20 ,and returns a formatted string: 'alice:25 years, bob:30 years".

def merge_profiles(**users):
    for key, value in users.items():
        print(f'{key}: {value} years')

merge_profiles(alice = 25, bob=20, santosh=23)

print(sorted('santosh'))