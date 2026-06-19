# create a class where private,protected,public attributes should be meaningfully use
# and implement either private or protected in any of method of that class 
# and report does encapsulation effects method of class or  not.


class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        # Public attribute
        self.account_holder = account_holder

        # Protected attribute
        self._account_number = account_number

        # Private attribute
        self.__balance = balance

    # Public method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}")

    # Public method
    def withdraw(self, amount):
        if amount > 0 and self.__verify_balance(amount):  # private method used
            self.__balance -= amount
            print(f"Withdrawn Rs.{amount}")
        else:
            print("Insufficient balance!")

    # Private method
    def __verify_balance(self, amount):
        return self.__balance >= amount

    # Public method
    def show_balance(self):
        print(f"Current Balance: Rs.{self.__balance}")


# Creating object
account = BankAccount("Samir", "ACC12345", 5000)

# Accessing public attribute
print(account.account_holder)

# Accessing methods
account.deposit(1000)
account.withdraw(2000)
account.show_balance()

# Protected attribute (possible but not recommended)
print(account._account_number)

# Private attribute (will cause error)
# print(account.__balance)

#create a parent class vehicle and sub class as Car and Bike.
#Inherite the Vehicle class to subclass with some defined methods
#like start_engine and some know attributes. add some specific methods and 
#attributes in sub class as well as

# Parent Class
class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"{self.brand}'s engine has started.")

    def stop_engine(self):
        print(f"{self.brand}'s engine has stopped.")


# Child Class: Car
class Car(Vehicle):
    def __init__(self, brand, fuel_type, num_doors):
        super().__init__(brand, fuel_type)
        self.num_doors = num_doors

    def open_trunk(self):
        print(f"{self.brand}'s trunk is now open.")

    def car_info(self):
        print(
            f"Car Brand: {self.brand}, Fuel Type: {self.fuel_type}, Doors: {self.num_doors}"
        )


# Child Class: Bike
class Bike(Vehicle):
    def __init__(self, brand, fuel_type, bike_type):
        super().__init__(brand, fuel_type)
        self.bike_type = bike_type

    def wheelie(self):
        print(f"{self.brand} is performing a wheelie!")

    def bike_info(self):
        print(
            f"Bike Brand: {self.brand}, Fuel Type: {self.fuel_type}, Type: {self.bike_type}"
        )


# Creating Objects
car1 = Car("Toyota", "Petrol", 4)
bike1 = Bike("Yamaha", "Petrol", "Sports")

# Using inherited methods
car1.start_engine()
bike1.start_engine()

# Using subclass-specific methods
car1.open_trunk()
bike1.wheelie()

# Display information
car1.car_info()
bike1.bike_info()

# Stopping engines
car1.stop_engine()
bike1.stop_engine()

# create a class if human being and sub class Male and female with proper inheritance
# so that we can utilized inherited methods and attributes
# as well as add attributes methods to sub class 

# Parent Class
class HumanBeing:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Child Class: Male
class Male(HumanBeing):
    def __init__(self, name, age, beard_style):
        super().__init__(name, age)
        self.beard_style = beard_style

    def shave(self):
        print(f"{self.name} is shaving his {self.beard_style} beard.")

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Beard Style: {self.beard_style}")


# Child Class: Female
class Female(HumanBeing):
    def __init__(self, name, age, hair_length):
        super().__init__(name, age)
        self.hair_length = hair_length

    def braid_hair(self):
        print(f"{self.name} is braiding her {self.hair_length} hair.")

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Hair Length: {self.hair_length}")


# Creating Objects
male1 = Male("Pranit", 25, "French Cut")
female1 = Female("Sandhya", 23, "Long")

# # Using inherited methods
# male1.introduce()
# male1.eat()
# male1.sleep()

# female1.introduce()
# female1.eat()
# female1.sleep()

# Using subclass-specific methods
# male1.shave()
# female1.braid_hair()

# # Display details
# male1.show_details()
# female1.show_details()

# class Vehicle:
#     def start_engine(self):
#         print("Engine started")

# class Car(Vehicle):
#     pass

# car = Car()
# car.start_engine()
