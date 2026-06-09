# Accumulating information of student
name = input("Enter name of student: ")
roll = input("Enter roll no. of student: ")

print("Enter marks of following three subjects: ")

marks1 = float(input("Math: "))
marks2 = float(input("English: "))
marks3 = float(input("Science: "))
marks4 = float(input("Computer Science: "))

# Student dictionary

student = {
    'name': name,
    'roll': roll,
    'Math': marks1,
    'English': marks2,
    'Science': marks3,
    'Computer Science': marks4
}

#Marks dictionary
marks = {
    1: marks1,
    2: marks2,
    3: marks3,
    4: marks4
}

#validate marks
for i in marks:
    if marks[i] < 0 or marks[i] > 100:
        print(f"\n:( Invalid marks {marks[i]} entered)")
        print("Marks must be between 0 and 100")
        exit()

total = marks[1] + marks[2] + marks[3]

percentage = total / 3

print(total)
print(percentage)
