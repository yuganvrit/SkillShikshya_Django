class StudentSystem:
    def __init__(self, name, total_fee, monthly_fee, id):
        self.name = name
        self.__total_fee = total_fee
        self.__monthly_fee = monthly_fee
        self._id = id

    def __fee(self):    
        return f"{self.name} is the name of the student"
    
    def monthly(self):
        return f"{self.__monthly_fee} is the monthly fee"
    

obj1 = StudentSystem("Sahil", 100000, 10000, 100)
# print(obj1.__fee()) 
print(obj1.monthly())