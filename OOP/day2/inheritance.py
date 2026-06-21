# inheritance

class Animal:
    def __init__(self, legs_count, back_bone, can_fly, horn):
        self.legs_count = legs_count
        self.back_bone = back_bone
        self.can_fly = can_fly
        self.horn = horn
    def eat(self, name):
        return f"{name} is eating."
    
class Dog(Animal):
    def __init__(self, tail, legs_count, back_bone, can_fly, horn):
        super().__init__(legs_count, back_bone, can_fly, horn)
        self.tail = tail

    def bark(self, name):
        return f"{name} is barking"
    
tommy = Dog(5, 4, True, False, False)
print(tommy.tail)
print(tommy.eat("tommy"))