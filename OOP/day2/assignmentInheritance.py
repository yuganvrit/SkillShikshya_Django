class Vehicle:
    def __init__(self, name, id, color):
        self.name = name
        self.id = id
        self.color = color

    def start_engine(self):
        return f"{self.color} colored {self.name}'s engine has started"
    
class Car(Vehicle):
    def __init__(self, name, id, color, wheels):
        super().__init__(name, id, color)
        self.wheels = wheels

    def start(self):
        return f"{self.name} is speeding. It has {self.wheels} wheels"
    
ford = Car("ford", 10, "white", 4)
print(ford.start_engine())
print(ford.start())
    