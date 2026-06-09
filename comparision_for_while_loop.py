# Side-by-side comparision
# FOR LOOP - Best when you know the range
print("Using for loop:")
for i in range(1, 6):
    print(i)

# WHILE LOOP - More verbose but works
print("Using while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# sum of list of elements

numbers = [10, 20, 30, 40, 50]

# FOR LOOP - Clean and simple
total = 0
for num in numbers:
    total += num
print(f"Sum (for): {total}")

# WHILE LOOP - Need index management
total = 0
index = 0
while index < len(numbers):
    total += numbers[index]
    index += 1
print(f"Sum (while): {total}")  

# real-world scenarios
# 1. Processing all items in a collection
emails = ["a@test.com", "b@test.com", "c@test.com"]
for email in emails:
    send_email(email)

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

#when to use while loop
# 1. User menu (run until user exits)
choice = ""
while choice != "exit":
    choice = input("Enter command (exit to quit): ")
    if choice == "help":
        print("Available commands: help, exit")

# 2. Game loop (runs until game over)
health = 100
while health > 0:
    damage = int(input("Enter damage: "))
    health -= damage
    print(f"Health: {health}")
print("Game Over!")

# 3. Waiting for condition to change
import random
target = random.randint(1, 100)
guess = None
attempts = 0
while guess != target:
    guess = int(input("Guess number: "))
    attempts += 1
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
print(f"Correct! Took {attempts} attempts")

# 4. Processing data until end
data_stream = [1, 2, 3, -1, 4, 5]  # -1 is sentinel
index = 0
while data_stream[index] != -1:
    print(f"Processing: {data_stream[index]}")
    index += 1

# 5. Retry mechanism
max_retries = 3
retry_count = 0
success = False

while retry_count < max_retries and not success:
    try:
        result = some_operation()
        success = True
    except:
        retry_count += 1
        print(f"Retry {retry_count}/{max_retries}")


