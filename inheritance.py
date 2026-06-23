# # # # class A:
# # # #     def greet(slef):
# # # #         return'hello'
    

# # # # class B:
# # # #     def greet(self):
# # # #         return'hi'
    
# # # # class C(A,B):
# # # #     pass

# # # # c_object= C()

# # # # print(c_object.greet())


# # # ## create aparent and child class and show a example of ovveriding
# # # #demonstrate a example of MRO with order of MRO

# # # class Vehicle:
# # #     def start(self):
# # #         return 'engine start'
    

# # # class Car(Vehicle):
# # #     def start(self):
# # #         return'engine start'
    
# # # class Bike(Vehicle):
# # #     def start(self):
# # #         return'cold start'
    

# # # BMW= Car()
# # # print(BMW.Car())




# # class SwimMixin:
# #     def swim(self, animal_type):
# #         return f'{animal_type} is swimming'
    

# # class Duck(SwimMixin):
# #     pass

# # class Fish(SwimMixin):
# #     pass

# # nemo = Fish()
# # nemo.swim('fish')
# # print(nemo.swim('fish'))

# # donald = Duck()
# # donald.swim('duck')
# # print(donald.swim('duck'))


# class CreateUpdateDeleteMixin:
#     def add(self,data,info):
#         return data.append(info)

#     def update(self,data,update_data,id):
#         for d in data:
#             if d.get('id') == id:
#                 d.update(update_data)
#                 return d 
#         return f'{id} doesnot exit'

#     def delete(self,data,id):
#         for d in data:
#             if d.get('id') == id:
#                 data.remove(d)
#                 return data  
#         return f'{id} doesnot exit'




# class Students(CreateUpdateDeleteMixin):
#     def __init__(self,data):
#         self.data = data     #list of dictionary 


#     def add_student(self,info):
#         return self.add(self.data,info)
    

#     def update_student(self,updated_data,id):
#         return self.update(self.data,updated_data,id)
    

#     def delete_student(self,id):
#         return self.delete(self.data,id)
    

# data = [
#     {
#         'id':1,
#         'name':'ram',
#         'faculty':'BCT',
#         'fav_god':'krishna'
#     },
#     {
#         'id':2,
#         'name':'santosh',
#         'faculty':'BCE',
#         'fav_god':'Ram'
#     },
#     {
#         'id':3,
#         'name':'Tony',
#         'faculty':'CSIT',
#         'fav_god':'Shiva'

#     }
# ]
# student_engine = Students(data)
# print(student_engine.data)

# student_engine.add_student(
#     {
#         'id':4,
#         'name':'Shanks',
#         'faculty':'Architecture',
#         'fav_god':'Hanuman'
#     }
# )
# print(student_engine.data)

# student_engine.update_student({'faculty':'BCA'},4)
# print(student_engine.data[3])

# student_engine.delete_student(4)
# print(student_engine.data)



class CreateUpdateDeleteMixin:
    def add(self,data,info):
        return data.append(info)

    def update(self,data,update_data,id):
        for d in data:
            if d.get('id') == id:
                d.update(update_data)
                return d 
        return f'{id} doesnot exit'

    def delete(self,data,id):
        for d in data:
            if d.get('id') == id:
                data.remove(d)
                return data  
        return f'{id} doesnot exit'
    
class Teachers(CreateUpdateDeleteMixin):
    def __init__(self, data):
        self.data= data

    def add_teacher(self,info):
          return self.add(self.data,info)
    

    def update_teacher(self,updated_data,id):
        return self.update(self.data,updated_data,id)
    

    def delete_teacher(self,id):
        return self.delete(self.data,id)

    

data=[
    {
        'id':1,
        'name':'Thomas',
        'department':'Computer',
    },
    {
        'id':2,
        'name':'Alice',
        'department':'Civil',
    },
    {
        'id':3,
        'name':'Luffy',
        'department':'CsIT'
    },

]
teacher_engine=Teachers(data)

teacher_engine.add_teacher(
    {
        'id':4,
        'name':'Zoro',
        'department':'Python'
    }
)
print(teacher_engine.data)

teacher_engine.update_teacher({'name':'Yonko'},3)
print(teacher_engine.data)









