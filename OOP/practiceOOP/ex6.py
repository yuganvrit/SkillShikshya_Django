class Animal:
    def sound(self):
        return "Animal makes sound"

class Dog(Animal):
    def sound(self):
        return "Dog barks"


elephant = Animal()
print(elephant.sound())
tommy = Dog()
print(tommy.sound())