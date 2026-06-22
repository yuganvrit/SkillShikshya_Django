class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def perimeter(self):
        p = 2 * (int(self.length) + int(self.breadth))
        return p
    
    def area(self):
        p = int(self.length) * int(self.breadth)
        return p
    
rec1 = Rectangle(2, 3)
print(rec1.perimeter())
print(rec1.area())