class Dog:
    def __init__ (self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        return self.name + " " + "says woof!"
    

rex = Dog("Rex", "Husky", 4)
print(rex.bark())


class Cat:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
    
    def sound(self):
        return self.name + ' ' + "says Meow!"
    
kitty = Cat("Kitty", "Black", "Persian")
print(kitty.sound())
print(kitty.name)
print(kitty.breed)
print(kitty.color)

class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def fly(self):
        return self.name + ' ' + "flew!"
    

bird1 = Bird("parrot", "Brown")
print(bird1.fly())