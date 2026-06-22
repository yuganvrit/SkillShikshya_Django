class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating!"
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def bark(self):
        return f"{self.name} is barking!"
    
tommy = Dog("Tommy")
print(tommy.eat())
print(tommy.bark())