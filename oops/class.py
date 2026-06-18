class Cat:
    def __init__(self, name, color, breed):
        self.name=name
        self.color = color
        self.breed = breed

    
    def sound(self):
        print(f'{self.name} meows')




# cat1 = Cat('kitty', 'white', 'persian')
# print(cat1.name)
# print(cat1.color)
# print(cat1.breed)
# print(cat1.sound())


# class Bird:
    
#     def __init__(self, name, breed, color):
#         self.name = name
#         self.breed = breed
#         self.color = color

    
#     def fly(self):
#         print(f'{self.name} is flying...')

# bird1 = Bird('chara', 'pigeon', 'blue')

# print(bird1.name)
# print(bird1.breed)
# print(bird1.color)
# print(bird1.fly())


# #Verify the age of the dog before updating from outside.

# class Cat:
#     def __init__(self, name, color, breed, age):
#         self.name=name
#         self.color = color
#         self.breed = breed
#         self.__age = age

    
#     def sound(self):
#         print(f'{self.name} meows')

    
#     # # @property
#     # def age(self):
#     #     return self.__age
    
#     # # @age.setter
#     # def age(self, value):
#     #     if value >0 and value <10:
#     #         self.__age = value
#     #     else:
#     #         print("Value error")

# cat1 = Cat('kitty', 'white', 'kat', 14)
# print(cat1.__age)

# cat1.__age = 25


#encapsulation + inheritance
#create a class where private, public and protected attributes should be used meaning fully and implement either private or protected in any of methods of that class and report , if encapsulation effects methods of a class or not


class Facebook:
    def __init__(self, profile_name, posts,password ):
        self.profile_name = profile_name
        self._posts = posts
        self.__password = password

    def create_post(self):
        print(f'{self.profile_name} posted {self._posts}')

    def change_password(self, password):
        self.__password = password

    def show_password(self):
        return self.__password

account1 = Facebook('santosh', '"Hello! everyone this is santosh"', 'fb12345')

print(account1.profile_name)
print(account1.create_post())
print(account1.show_password())
print(account1.__password)


class Animal:
    def __init__(self, legs, has_backbone, can_fly):
        self.legs = legs
        self.has_backbone = has_backbone
        self.can_fly = can_fly
    
    def eat(self, name):
        return f'{name} is eating...'
    
class Dog(Animal):
    def __init__(self, legs, has_backbone, can_fly, name):
        super().__init__(legs, has_backbone, can_fly)

        self.name = name

    def sound(self):
        return f'{self.name} is making sound....'
    
tommy = Dog(4, True, False, 'tommy')
print(tommy.sound())


class HumanBeing:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f'{self.name} is speaking...'
    
    def check_age(self):
        return f'{self.name} is {self.age} years old'
    

class Male(HumanBeing):
    def __init__(self, name, age, gender, standard):
        super().__init__(name, age)

        self.gender = gender
        self.standard = standard

    def introduction(self):
        return f'My name is {self.name}. I am a {self.gender}'
    
    def check_standard(self):
        return f'{self.name} studies in {self.standard}'

class Female(HumanBeing):
    def __init__(self, name, age, gender, greet):
        super().__init__(name, age)

        self.gender = gender
        self.greet = greet

    def greet(self):
        return f'{self.greet}! {self.name}'
    

