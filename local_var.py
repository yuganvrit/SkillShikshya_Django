# a local variable is created only inside the function. and can only be used there.

def my_func():
    x = 10
    print(x) # local var.
my_func()    
print(x) # gives error becz local var. is printed only inside the function.

# using both local and var.

x = 10
def my_function():
    y = 20
    print(y)
    print(x)
my_function()
print(x)    

