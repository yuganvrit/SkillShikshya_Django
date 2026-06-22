class SwimMixin:
    def swim(self,animal_type):
        return f'{animal_type} is swiming'
    

class Duck(SwimMixin):
  pass

class Fish(SwimMixin):
   pass
  

nemo = Fish()
print(nemo.swim('fish'))



donald = Duck()
print(donald.swim('duck'))






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




class Students(CreateUpdateDeleteMixin):
    def __init__(self,data):
        self.data = data     #list of dictionary 


    def add_student(self,info):
        return self.add(self.data,info)
    

    def update_student(self,updated_data,id):
        return self.update(self.data,updated_data,id)
    

    def delete_student(self,id):
        return self.delete(self.data,id)
    








# class Teachers(CreateUpdateDeleteMixin):
#     def __init__(self,data):
#         self.data = data     #list of dictionary 




data = [
    {
        'id':1,
        'name':'aryan',
        'faculty':'ai/ml',
        'fav_god':'krishna'
    },
    {
        'id':2,
        'name':'santosh',
        'faculty':'cybersecurity',
        'fav_god':'Ram'
    },
    {
        'id':3,
        'name':'sakshyam',
        'faculty':'deveops',
        'fav_god':'Shiva'

    }
]
student_engine = Students(data)
print(student_engine.data)

student_engine.add_student(
    {
        'id':4,
        'name':'shahil',
        'faculty':'Django',
        'fav_god':'Hanuman'
    }
)
print(student_engine.data)

student_engine.update_student({'faculty':'Computer Vision'},4)
print(student_engine.data[3])

student_engine.delete_student(4)
print(student_engine.data)

