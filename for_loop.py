# used when u know how many times to iterate
# basic syntax
# sequence = ['1', '2', '3']
# for variable in sequence:

# Examples of for loop
# 1. Loop through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# Output: apple, banana, cherry

# # 2. Loop using range() - do something 5 times
# for i in range(5):
#     print(f"Iteration {i}")
# # Output: 0,1,2,3,4

# # 3. Loop through string
# for char in "Python":
#     print(char)
# # Output: P,y,t,h,o,n

# # 4. Loop through dictionary
# student = {"name": "John", "age": 20, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")

# # 5. Loop with enumerate (get index and value)
# colors = ["red", "green", "blue"]
# for index, color in enumerate(colors):
#     print(f"{index}: {color}")

# # 6. Nested for loop
# for i in range(3):
#     for j in range(2):
#         print(f"i={i}, j={j}")



# Real world Scenarios
# when to use for loop
# 1. Processing all items in a collection
send_email = input('Enter a mail id: ')
emails = ["a@test.com", "b@test.com", "c@test.com"]
for email in emails:
    send_email(email)
    print(f"You entered: {send_email}")

# 2. Fixed number of iterations
for i in range(10):
    print(f"Step {i+1}")

# 3. Reading all lines of a file
with open("file.txt") as file:
    for line in file:
        print(line.strip())

# 4. String manipulation
text = "Hello World"
for char in text:
    if char.isupper():
        print(f"Uppercase: {char}")

# 5. Creating a new list from existing
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]

#common for loop pattern

# Pattern 1: Loop with index
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Pattern 2: Loop with enumerate (better)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Pattern 3: Loop backwards
for i in range(5, 0, -1):
    print(i)  # 5,4,3,2,1

# Pattern 4: Loop with step
for i in range(0, 10, 2):
    print(i)  # 0,2,4,6,8

# Pattern 5: Loop through multiple lists (zip)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
