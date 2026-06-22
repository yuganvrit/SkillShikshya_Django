class Shape:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def define(self):
        return f"The shape {self.name} is a {self.type}."

class Circle(Shape):
    def __init__(self, name, type):
        super().__init__(name, type)

    def radius(self, radius):
        return f"The radius of the circle is {radius}"
    
    def area(self, radius):
        a = 2 * 3.143 * radius
        return f"The area of the circle is {a}"
    
shape1 = Circle("shape1", "circle")
print(shape1.define())
print(shape1.radius(5))
print(shape1.area(5))