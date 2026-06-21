class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        return f"{self.name} says woof!"
    

ramey = Dog("Ramey", 'Golden Retriever', 2)
print(ramey.bark())

shyamey = Dog("Shyamey", "Poodle", 3)
print(shyamey.bark())