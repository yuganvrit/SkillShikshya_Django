class Cat:
    def __init__(self,name,color,breed):
        self.__name = name 
        self.color = color 
        self.breed = breed

    def sound(self):
        return f'{self.__name} meow meow'
    

persian_cat = Cat('luna','white','persian')
#print attributes 
print(persian_cat.sound())



class BankAccount:
    def __init__(self, holder, balance, pin):
        self.holder = holder          # public  — open to all
        self._balance = balance       # protected — subclasses use it
        self._transactions = []       # protected — the audit log
        self.__pin = pin              # private — name-mangled, hidden

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(("deposit", amount))   # log stays in sync

    def check_pin(self, attempt):
        return attempt == self.__pin
    

#Inheritance

class Animal:
    def __init__(self,legs_count,backbone,can_fly,horn):
        self.legs_count = legs_count
        self.backbone= backbone
        self.can_fly = can_fly 
        self.horn = horn

    
    def eat(self,name):
        return f'{name} is eating'


class Dog(Animal):
    def __init__(self,tail,legs_count,backbone,can_fly,horn):
        super().__init__(legs_count,backbone,can_fly,horn)
        self.tail=tail


    def bark(self,name):
        return f'{name} is barking'




#classwork
#create a class of Human Being and sub class like Male and Female  with proper inheritance 
#so that we can utilize inherited attributes and methods
#as well as add some methods and attributes specific to sub classes 