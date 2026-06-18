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
    def __init__(self, brand, color, ):
        super().__init__(brand, color)