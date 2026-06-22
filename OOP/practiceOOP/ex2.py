class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def introduce(self):
        return f"Hi, my name is {self.name} and I study in grade {self.grade}. I am {self.age} years old."

st1 = Student("Sahil", 22, "Bachelors")
print(st1.introduce())