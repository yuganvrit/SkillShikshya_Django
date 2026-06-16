# Data comprehension is a concise way to create lists, sets, or dictionaries in Python.
# It allows you to generate a new collection by applying an expression to each item in an iterable, optionally filtering items using a condition.
# Types of comprehensions in Python:
# 1. List Comprehension 
# 2. Set Comprehension
# 3. Dictionary Comprehension
# List Comprehension
squares = [x**2 for x in range(10)]   
print(squares)

# with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares) 


# Set Comprehension
unique_squares = {x**2 for x in range(10)}  
print(unique_squares)

#Dictionary Comprehension
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

# Examples
student_names = ['sabin', 'ram', 'shyam']
student_grades = {name: 'A' for name in student_names}
print(student_grades)

# Convert set to sorted list
unique_squares = sorted({x**2 for x in range(10)})
print(unique_squares) # to print output in ordered list in set comprehension we can use sorted() function to sort the output and convert it to list.



