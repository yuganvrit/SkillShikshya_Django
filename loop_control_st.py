#loop control statements

# break - exit loop completely
for i in range(10):
    if i == 5:
        break
    print(i)  # 0,1,2,3,4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0,1,3,4

# else - executes if loop didn't break
for i in range(3):
    print(i)
else:
    print("Loop completed without break")

# Works with while too
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed")

# common mistakes and solution

# MISTAKE 1: Infinite while loop
# WRONG
count = 0
while count < 5:
    print(count)
    # Missing count += 1 → Infinite loop!

# CORRECT
count = 0
while count < 5:
    print(count)
    count += 1

# MISTAKE 2: Modifying list while iterating
# WRONG
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# CORRECT - Iterate over copy
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

# MISTAKE 3: Off-by-one errors
# WRONG
for i in range(1, 5):  # Only goes to 4
    print(i)  # 1,2,3,4

# CORRECT - for inclusive range
for i in range(1, 6):  # Goes to 5
    print(i)  # 1,2,3,4,5     