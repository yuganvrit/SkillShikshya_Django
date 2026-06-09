# used when you don't know how many times to iterate
# 1. Simple counter
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # IMPORTANT: Update condition
# Output: 0,1,2,3,4

# 2. User input until valid
password = ""
while password != "secret":
    password = input("Enter password: ")
    if password != "secret":
        print("Wrong password, try again")
print("Access granted!")

# 3. Game loop
playing = True
score = 0
while playing:
    print(f"Score: {score}")
    answer = input("Continue? (y/n): ")
    if answer == 'n':
        playing = False
    else:
        score += 10

# 4. Sum numbers until user enters 0
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print(f"Total: {total}")

# 5. While with else (executes if loop completes normally)
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed without break")

#common while loop pattern

# Pattern 1: Infinite loop with break (valid use case)
while True:
    command = input("Enter command: ")
    if command == "quit":
        break
    print(f"Executing: {command}")

# Pattern 2: Sentinel-controlled
total = 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Total: {total}")

# Pattern 3: Flag-controlled
is_running = True
while is_running:
    choice = input("Continue? (y/n): ")
    if choice.lower() == 'n':
        is_running = False

# Pattern 4: Counter-controlled
i = 0
while i < 5:
    print(i)
    i += 1

# Pattern 5: Try-until-success
import random
found = False
attempts = 0
while not found:
    attempts += 1
    if random.randint(1, 100) == 50:
        found = True
print(f"Found after {attempts} attempts")

