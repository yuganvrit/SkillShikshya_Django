# # map(), filter() and reduce() are higher order function. a func that takes 

# lst = [1,2,3,4,5,6,7]

# def square(x):
#     return x*x

# squared_number = map(square, lst)

# # squared_number = (map(lambda x:x*x, lst))
# print(list(squared_number))



# #use map method that takes a list of numbers and returns the length of each string using map function

# strlst = ['hello', 'world', 'santosh']

# def strlength(n):
#     return len(n)

# print(list(map(strlength, strlst)))

#take a lst of numbers if even reeturn true else false.

def check_even_odd(n):
    if n%2 == 0:
        return True
    return False

numlst = [1,2,3,4,5]

print(list(map(check_even_odd, numlst)))
# print(list(map(lambda x: , numlst)))


#return a dict with their length 
strdict = {'name': 'santosh', 'address':'tokha'}

#return 'name':len('john')


#reduce function.

from functools import reduce

#=>reduces only one output.

def total_sum(x, y):
    return x+y

sum = reduce(total_sum, numlst)
print(sum)


#create a list and use reduce function to find the product of all elements in list.

def total_product(x,y):
    return x*y

print(reduce(total_product, numlst))

#there is a nested list containing a list as a child using the reduce function flatten the list.

nested_lst = [[1,2,3,4], [5,6,7,8], [9,19,11,34]]

def flatten_lst(x,y):
    # emplst = []
    # for i in x:
    #     emplst.append(i)
    # for i in y:
    #     emplst.append(i)


    return [*x, *y]

output = reduce(flatten_lst, nested_lst)
print(output)