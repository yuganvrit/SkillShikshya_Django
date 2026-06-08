playlist = ['song1', 'song2', 'song3']

engine = iter(playlist)

print(next(engine))
print(next(engine))
print(next(engine))

for song in playlist:
    print(song)


sakshyam_marks_sheet = [80, 50, 60, 90, 90, 78]
for marks in sakshyam_marks_sheet:
    if marks >= 90:
        print("Grade A")
    elif marks >=80:
        print("Grade B")
    elif marks >= 70:
        print("Grade C")
    else:
        print("Grade D")

#Task 1:
grades = [88, 90, 99, 77, 66]
iter_grades = grades.__iter__()

print(next(iter_grades))
print(next(iter_grades))
print(next(iter_grades))
print(next(iter_grades))
print(next(iter_grades))

#Task 2:
names = ['Sakshyam', 'Santosh', 'Samir', 'Pranita', 'Prince']

for name in names:
    print(f'Hello {name}')

#Task 3:
#1
for numbers in range(21):
    print(numbers)

#2
num = list(range(1, 11))
num_list = num[::-1]
for n in num_list:
    print(n)

#3
multiplication_table = list(range(1, 11))
for i in multiplication_table:
    print(f"7 x {i} = {7*i}")

#Task 4:
scores = [78, 92, 55, 88, 64, 91, 73]

#1
total = 0
average = 0
for i in scores:
    total += i
    average = total / len(scores)
    print(f'Total: {total} and Average: {average}')

#2
count = 0
for passing in scores:
    if passing >= 60:
        print(passing)
        count += 1
    else:
        break
print(count)

#3
scores.sort()
print(scores)
