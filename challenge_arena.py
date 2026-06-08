lst = [8, 6, 4, 7, 9, 10, 15, 20, 18]

largest = lst[0]
second_largest = lst[1]

for i in lst:
    if i>largest:
        largest = i

for j in lst:
    if j>second_largest and j<largest:
        second_largest = j

print(second_largest)


check_number = 18
count = 0

for i in range(2, 19):
    if check_number % i == 0:
        count += 1

if count == 0:
    print("Prime number")
else:
    print('Composite Number')