# Default parameters
# Gives a default value if user doesn't pass anything

# def greet(name="Guest"):
#     print("Hello", name)

# greet()
# greet("Samir")

# 🔥 2. *args (Non-keyword arguments)

# 👉 Takes any number of positional arguments

# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5))

# # note:👉 *args becomes a tuple.

# #🔥 3. **kwargs (Keyword arguments)

# # 👉 Takes any number of named arguments
# def student(**data):
#     print(data)

# student(name="Samir", age=20, city="Kathmandu")

# #note:  kwargs become a dict.

# # 🔥 4. Keyword-only arguments

# # 👉 Must be passed using name

# def info(*, name, age):
#     print(name, age)

# info(name="Samir", age=20)
# # info("Samir", 20) -> error becz * sign indicates keyword only arguments

# #🔥 5. Positional-only arguments (Python 3.8+)

# # 👉 Cannot use names, only position

# def multiply(a, b, /):
#     return a * b

# print(multiply(2, 3))

# 6. Combination of all (real advanced form)

# def demo(a, b, /, c, d=10, *args, e, **kwargs):
#     print(a, b, c, d, args, e, kwargs)

# demo(1, 2, 3, e=5)    

# for char in "Python":
#     print(char)
    

# def greet(*,name,age):
#     print(name,age)
# greet(name='samir',age=28)


# **kwargs into dict.

    

# def greet(*, name, age):
#     person = {
#         "name": name,
#         "age": age
#     }
#     return person

# result = greet(name="Samir", age=28)
# print(result)

# wrong code -> because in dict we use (:) not (=)
# def greet(*,name , age):
#     person = {
#         'name' = name,
#         'age' = age,
#     }
#     return person
# result = greet(name = 'samir', age= 20)
# print(result)

# *,(used to force keyword only arg. after this)
def demo(a, b, *, c, d):
    print(a, b, c, d)
demo(1,2,c=3,d=4)    

# *args(positional arg. collector, non-key)

def demo(*args):
    print(args)
demo(1,2,3,4)    # output in tuple.

# ** kwargs(🔥 3. **kwargs (keyword arguments collector)

# Collects any number of keyword arguments into a dictionary.)
def demo(**kwargs):
    print(kwargs)
demo(name="Samir", age=28)    # output in dict.






