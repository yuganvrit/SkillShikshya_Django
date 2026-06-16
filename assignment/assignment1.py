# find the second largest number in the list without using max()twice.


list = [5, 2, 6, 9, 3]
largest = list[0]
second_largest = list[0]

for i in list:
    if i > largest:
        second_largest = largest  # Previous largest becomes second
        largest = i                # Update largest
    elif i > second_largest and i != largest:
        second_largest = i

print("Largest:", largest)
print("Second largest:", second_largest)
