# class BankAccount:
#     def __init__(self, holder, balance, pin):
#         self.holder = holder        #public
#         self._balance = balance     #protected
#         self._transitions = []      #protected
#         self.__pin = pin            #private

#     def deposit(self, amount):
#         self._balance += amount
#         self._transitions.append(("deposite", amount)) ## tuple use gareko kina vane transition viotra ko kura change garna mildaina

#     def check_pin(self, attempt):
#         return attempt == self.__pin
    



##classwork 
# ##create a class private protected and public attributes should be meaningfully and implement either private or protected in any of method of that class
# #and report does encapsulation effects method of class or not

class Car:
    def __init__(self, brand, model, engine_number):
        self.brand = brand                # Public
        self._model = model               # Protected
        self.__engine_number = engine_number  # Private

    def brand_info(self):
        return self.brand

    def model_info(self):
        return self._model

    def engine_info(self):
        return self.__engine_number


cars = Car("BMW", "M4", 12321)

print(cars.brand_info())
print(cars.model_info())
print(cars.engine_info())
     


    



# class Animal:
#     def __init__(self, leg_count, backbone, can_fly ,horn):
        
#         self.leg_count = leg_count
#         self.backbone = backbone
#         self.can_fly = can_fly
#         self.horn = horn

#     def eat(self,name):
#         return f'{name} is eating'
    
# class Dog(Animal):
#     def __init__(self, tail,leg_count, backbone, can_fly, horn):
#         super().__init__(leg_count, backbone, can_fly, horn)
#         self.tail = tail


#     def bark(self, name):
#         return f'{name} is barking'
    
# tommy = Dog(5, 4 ,True, True, False)
# print(tommy.eat('tommy'))


## create a class of human being and sub class like male and female with proper inheritence
#so that we can  add some method and attributes specific to sub class

# class HumanBeing:
#     def __init__(self, leg_count, eye_count, can_walk):
#         self.leg_count = leg_count
#         self.eye_count = eye_count
#         self.can_walk = can_walk

#     def walking(self, name):
#         return f'{name} is walking on road'
    
# class Male(HumanBeing):
#     def __init__(self, mouth,leg_count, eye_count, can_walk):
#         super().__init__(leg_count, eye_count, can_walk)
#         self.mouth = mouth

#     def eating(self, name):
#         return f'{name} is eating rice'


# class Female(HumanBeing):
#     def __init__(self, mouth,leg_count, eye_count, can_walk):
#         super().__init__(leg_count, eye_count, can_walk)
#         self.mouth = mouth

#     def dancing(self, name):
#         return f'{name} is dancing'


# Ram = Male(2,2, True,True)
# Sita = Female(2,2, True,True)
# print(Ram.eating('Ram'))
# print(Sita.dancing('Sita'))

