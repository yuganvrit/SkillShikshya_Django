#performance comparision

import time

# For loops are generally faster for known iterations
numbers = list(range(1000000))

# FOR LOOP - Faster
start = time.time()
total = 0
for num in numbers:
    total += num
print(f"For loop time: {time.time() - start:.4f} seconds")

# WHILE LOOP - Slightly slower
start = time.time()
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
print(f"While loop time: {time.time() - start:.4f} seconds")