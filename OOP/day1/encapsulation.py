# encapsulation
# -------encap protects the data for eg if we create a class Bank normally like before we can edit the contents but after we use encap we can protect it so that it cannot be changed


# example
class Cat:
    def __init__(self, name, color, breed):
        self.__name = name   #private
        self._color = color  #protected
        self.breed = breed   #public
    
    def sound(self):
        return self.__name + ' ' + "says Meow!"   #but can be acessed from inside the class
    
cat1 = Cat("Luna", "White", "Persian")
print(cat1.__name) 
print(cat1._color)
print(cat1.sound())


class BankAccount:
    def __init__(self, holder, balance, pin):
        self.holder = holder
        self._balance = balance
        self._transactions = []
        self.__pin = pin