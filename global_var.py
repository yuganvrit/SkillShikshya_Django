# a global variable is created outside all function and can be used anywhere.

x = 20 # global var.
def my_function():
    print(x)

my_function()
print(x)    

# global keyword is used to modify a variable inside a function.

x = 10
def my_function():
    x = 20
    print(x)
my_function()    

# qns
x = 10
def my_function():
    x = 20
    print(x)
    print("inside:", x)

my_function()
print("outside:", x)

# global variable is mostly useful in updating counters
count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)

# updating global var. into local var.(with global key-> gives new global var, i.e same local var.)
mode = "light"

def switch():
    global mode # it tells python, i am not creating new local var. but updating previous global var.
    mode = "dark"# updating global var.(light-dark)

switch()# calls func.(global-local)
print(mode) # output -> dark

# without global key -> gives new local var. i.e same global var.
mode = "light"

def switch():
    mode = "dark"  # local variable, NOT global

switch() # creating new local var.(dark-light)
print(mode)# output -> light because of no global key

# # global keyword is not only for updating values but also to say to use global instead of creating new local
# # So it allows:
# # creating global variable inside function
# # modifying existing global variable
x = 10
def my_func():
    global x
    x = 20
my_func()
print(x)    

# 🧠 Simple memory trick:
# No global → new local variable
# With global → use original global variable

