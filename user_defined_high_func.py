


# # def global_divider(x,y):
# #     def divider(first_value,second_value):
# #         return first_value / second_value
# #     return divider

# # result = global_divider(9,9)
# # print(result(4,3))

# # def global_divider():
# #     def validator(first_value,second_value):
# #         def actual_divider(first,second):
# #             return first/second
# #         return actual_divider(first_value,second_value)
# #     return validator
# # result = global_divider()       # get the `validator` function
# # print(result(4, 3))             # call validator(4, 3) -> 1.3333333333333333

# # print(global_divider()(4, 3))   # 1.3333333333333333

# # def global_divider():
# #     def validator(first_value, second_value):
# #         return first_value / second_value
# #     return validator
# # result = global_divider()       # get the `validator` function
# # print(result(4, 3))             # call validator(4, 3) -> 1.3333333333333333

# # print(global_divider()(4, 3))

# # A decorator in Python is a function that takes another function as 
# # input, adds some extra functionality to it, and returns a new function — 
# # without permanently modifying the original function's code. It's basically a clean 
# # syntax for the "wrapper" pattern we discussed earlier

# # @my_decorator
# # def my_decorator
# # def say_hello():
# #     print("Hello!")

# # @my_decorator    
# # def my_decorator():
# #     def say_hello():
# #         print("Hello!")

# # say_hello = my_decorator(say_hello)


# # def my_decorator(func):
# #     def wrapper():
# #         print("Before the function runs")
# #         # func()
# #         print("After the function runs")
# #     return wrapper

# # @my_decorator
# # def say_hello():
# #     print("Hello!")

# # say_hello()

# # def my_decorator(func):
# #     def wrapper():
# #         print("Something before")
# #         func()
# #         print("Something after")
# #     return wrapper

# # @my_decorator
# # def say_hello():
# #     print("Hello!")

# # say_hello()

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)  # manual reassignment
say_hello()

# # from functools import wraps

# # def my_decorator(func):
# #     @wraps(func)
# #     def wrapper(*args, **kwargs):
# #         # Code to run BEFORE the original function
# #         print(f"Calling {func.__name__}...")
        
# #         result = func(*args, **kwargs)  # Call the original function
        
# #         # Code to run AFTER the original function
# #         print(f"{func.__name__} finished.")
        
# #         return result
# #     return wrapper


# # @my_decorator
# # def add(a, b):
# #     return a + b


# # print(add(3, 5))

# # from functools import wraps

# # def repeat(times):
# #     def decorator(func):
# #         @wraps(func)
# #         def wrapper(*args, **kwargs):
# #             result = None
# #             for _ in range(times):
# #                 result = func(*args, **kwargs)
# #             return result
# #         return wrapper
# #     return decorator


# # @repeat(3)
# # def greet(name):
# #     print(f"Hello, {name}!")


# # greet("Alice")

# from functools import wraps

# def validate_positive(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if any(arg < 0 for arg in args):
#             raise ValueError("All arguments must be positive")
#         return func(*args, **kwargs)
#     return wrapper


# @validate_positive
# def calculate_area(length, width):
#     return length * width


# print(calculate_area(4, 5))   # 20
# # print(calculate_area(-4, 5))  # raises ValueError

# #The outer function (my_decorator)
# #  accepts the function to be decorated. 
# # The inner function (wrapper) accepts *args, **kwargs 
# # so it works with any function signature.
# #  The wrapper calls the original function somewhere inside,
# # optionally adding logic before/after. @wraps(func) preserves the original function's name and
# #  docstring. The outer function returns the wrapper (not the result of calling it).
# #If you have a specific use case in mind, like logging
# # , authentication, caching, or retries, I can tailor
# #  a decorator for that exact purpose.

# def hello(name):
#     return f"hello {name}"

# print(hello('ram'))
# print(hello)