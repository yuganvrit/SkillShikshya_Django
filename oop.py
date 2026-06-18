class Cat:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def sound(self):
        return f"{self.name} say meow meow"

persian_cat = Cat('kitty','brown',5)
print(persian_cat.sound())

class Bird:
    def __init__(self,name, breed,color):
        self.name = name
        self.breed = breed
        self.color = color
    
    def fly(self):
        return f'{self.name} is flying'
    
parrot = Bird('parrot','wild_bird','green')
print(parrot.fly())