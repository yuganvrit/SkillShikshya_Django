class A:
    def greet(self):
        return "Hello"
    
class B:
    def greet(self):
        return "Hey"
    
class C(A, B):
    pass

c = C()
print(c.greet())

print(C.__mro__)
print(issubclass(A, object)) #classes are always the subclasses of objects even if its parent, its like baap ka baap




# ------------------------------------classwork------------------------------------------------------------
# q no 1---------------------------------------------------------------------------------------------------------
class Parent:
    def eat(self):
        return "Parent eats"
    
class Child(Parent):
    def eat(self):
        return "Child eats"
    
print("-------------------------output of question 1--------------------------------")
child1 = Child()
print(child1.eat())


# q no 2---------------------------------------------------------------------------------------------------------
class Father:
    def eat(self):
        return "Father eats"

class Mother:
    def eat(self):
        return "Mother eats"
    
class Child(Father, Mother): #which one is written first will be inherited
    pass
    
print("-------------------------output of question 2--------------------------------")
child1 = Child()
print(child1.eat())



# make st mixing method createst updatest


student_data = [
    {
        "id": 1,
        "name": "Aarav",
        "age": 20,
        "course": "Computer Science",
        "grade": "A"
    },
    {
        "id": 2,
        "name": "Sita",
        "age": 21,
        "course": "Information Technology",
        "grade": "B+"
    },
    {
        "id": 3,
        "name": "Rahul",
        "age": 19,
        "course": "Software Engineering",
        "grade": "A-"
    }
]


teachers = [
    {
        "id": 101,
        "name": "Mr. Sharma",
        "subject": "Python Programming",
        "experience_years": 8
    },
    {
        "id": 102,
        "name": "Ms. Rai",
        "subject": "Database Systems",
        "experience_years": 5
    },
    {
        "id": 103,
        "name": "Dr. Joshi",
        "subject": "Machine Learning",
        "experience_years": 12
    }
]


class studentMixin:
    def add(self, data, info):
        return data.append(info)
    
    def update(self, data, updated_data, id):
        for d in data:
            if d.get("id") == id:
                d.update(updated_data)
                return d
        return f"{id} not found!" 
    
    def delete(self, data, id):
        for d in data:
            if d.get('id') == id:
                data.remove(d)
                return data
        return f"{id} not found!"




class Student(studentMixin):
    def __init__(self, data):
        self.data = data
    
    def add_student(self,info):
        return self.add(self.data,info)
    
    def update_student(self,updated_data,id):
        return self.update(self.data,updated_data,id)

    def delete_student(self,id):
        return self.delete(self.data,id)
    
student_engine = Student(student_data)
print(student_engine.data)

student_engine.add_student(
    {
        'id':4,
        'name':'sahil',
        'faculty':'Django',
        'fav_god':'Hanuman'
    }
)
print(student_engine.data)

student_engine.update_student({'faculty':'Computer Vision'},4)
print(student_engine.data[3])

student_engine.delete_student(4)
print(student_engine.data)