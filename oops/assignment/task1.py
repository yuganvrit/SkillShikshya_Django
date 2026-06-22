#create a parent class vehicle and sub class as car and bike. use inheritance to inherit the vehicle class with some defined methods like start_engine() and some know attributes. add some specific methods and attributes in subclass as well

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def intro(self):
        return f'{self.brand} has {self.color} color'
    
    def start_engine(self):
        return f'{self.brand} is starting....'
    
    def stop_engine(self):
        return f'{self.brand} is stopping...'
    
class Car(Vehicle):
    def __init__(self, brand, color, doors, seats):
        super().__init__(brand, color)
        self.doors = doors
        self.seats = seats

    def car_info(self):
        return f'{self.brand} has {self.color} color and {self.doors} doors'
    
    def get_seats(self):
        return f"I'm {self.brand}. I have {self.seats} seats"

    

class Bike(Vehicle):
    def __init__(self, brand, color, wheels):
        super().__init__(brand, color)
        self.wheels = wheels

    def intro(self):
        return f"{self.brand} has {self.color} color and {self.wheels} wheels"
    


bike = Bike('TVS', 'black', 2)

print(bike.start_engine())
print(bike.intro())

car = Car('Porsche', 'red', 2, 2)

print(car.car_info())