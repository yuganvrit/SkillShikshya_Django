# map(), filter() and reduce() are higher order function. a func that takes 

lst = [1,2,3,4,5,6,7]

def square(x):
    return x*x

squared_number = map(square, lst)

# squared_number = (map(lambda x:x*x, lst))
print(list(squared_number))



#use map method that takes a list of numbers and returns the length of each string using map function

strlst = ['hello', 'world', 'santosh']

def strlength(n):
    return len(n)

print(list(map(strlength, strlst)))

#take a lst of numbers if even reeturn true else false.

def check_even_odd(n):
    if n%2 == 0:
        return True
    return False

# numlst = [1,2,3,4,5]

# print(list(map(check_even_odd, numlst)))
# print(list(map(lambda x: , numlst)))


#return a dict with their length 
strdict = {'name': 'santosh', 'address':'tokha'}

#return 'name':len('john')
