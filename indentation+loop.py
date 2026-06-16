# return inside loop
# 🔴 If inside loop:
# return happens early → function stops immediately
def sum_natural_numbers(*args):
    total = 0
    for element in args:
        total += element
        return total   # inside loop

result = sum_natural_numbers(1,2,3,4,5)
print(result) # output-> 1

# return outside loop
#🟢 If outside loop:
# loop completes first → then return happens

def sum_natural_numbers(*args):
    total = 0
    for element in args:
        total += element
    return total   

result = sum_natural_numbers(1,2,3,4,5)
print(result) # output-> 15

def sum_natural_numbers(*args):
    for element in args:
         total = 0
         total += element
         return total   

result = sum_natural_numbers(1,2,3,4,5)
print(result) #  output-> 1   

def sum_natural_numbers(*args):
    for element in args:
         total = 0
         total += element
    return total   

result = sum_natural_numbers(1,2,3,4,5)
print(result) #  output-> 5