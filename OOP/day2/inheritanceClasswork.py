class Human:
    def __init__(self, name, height, weight, color):
        self.name = name
        self.height = height
        self.weight = weight
        self.color = color
    
    def work(self, job):
        return f"This human works as a {job}"
    
class Male(Human):
    def __init__(self, name, height, weight, color, age, gender):
        super().__init__(name, height, weight, color, age, gender)
        self.age = age
        self.gender = gender

    def description(self):
        return f"{self.name} is a {self.gender}. {self.name} is {self.height} tall"
    
class Female(Human):
    def __init__(self, name, height, weight, color, age, gender):
        super().__init__(name, height, weight, color, age, gender)
        self.age = age
        self.gender = gender

    def description(self):
        return f"{self.name} is a {self.gender}. {self.name} is {self.height} tall"
    
    def hobbies(self, hobby):
        return f"{self.name}'s hobby is {hobby}"
    
ram = Male("Ram", "6ft", 80, "brown", 22, "Male")
print(ram.description())
print(ram.work("Economist"))

# sita = Female("Sita", "5ft", 50, "white", 21, "Female")
