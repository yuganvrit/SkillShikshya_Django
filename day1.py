def add_num(a,b):
    return a+b

add_num(1,2)


def add_list(my_list = []):
    my_list.append("hello")
    return my_list     #this returns and appends "hello" everytime i call this function

add_list() #["hello"]
add_list() #["hello", "hello"]
add_list() #["hello", "hello", "hello"]

# so  to debyug this we can use it like this. 

def new_list(n_list= None):
    if n_list == None:
        n_list = []
        n_list.append("hello")
    return n_list

new_list()  #this now solves that bug from before.


def info():
    information= "hello world"
    print(f"this is inside the info function {information}")

info()