class Animal:
    def sound(self):
        return "Animal makes sound"

class Dog(Animal):
    def sound(self): #if you want to use parents method + child use super
        super().sound()
        return "Dog barks"


elephant = Animal()
print(elephant.sound())
tommy = Dog()
print(tommy.sound())