# Dictionary in Python
# A dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. 
# The keys must be unique and immutable (e.g., strings, numbers, tuples), while the values can be of any type.
# my_dict = {
#     "name": "Samir",
#     "age": 30,
#     "city": "Kathmandu",
#     "college": "TU"
# }
# print(my_dict)
# print(type(my_dict))
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["city"])
# print(my_dict["college"])

#adding new key-value pair to the dictionary
# my_dict["gender"] = "Male"
# print(my_dict)

#accessing value using get() method
# print(my_dict.get("name"))  
# print(my_dict["name"])
# print(my_dict.get("age"))
# print(my_dict.get("city"))
# print(my_dict.get("college"))
# print(my_dict.get("gender"))

# #updating value in dictionary
# my_dict["name"] = "Samir Shrestha"
# print(my_dict)  

#creating a empty dictionary
# empty_dict = {}
# print(empty_dict)   
# print(type(empty_dict)) 

#fetches from the keys from the dictionary

# print(my_dict.keys())   
# print(my_dict.values())
# print(my_dict.items())

#pop method to remove a key-value pair from the dictionary
# my_dict.pop("gender")
# print(my_dict)

#pop item method to remove the last inserted key-value pair from the dictionary
# my_dict.popitem()   
# print(my_dict)

#merging two dictionaries

# student_sub_info = {
#     'name' : 'sabin',
#     'grade' : 'A',
#     'address' : 'Kathmandu'
# }

#these are the three ways to merge two dictionaries in python
# | method
# print(my_dict | student_sub_info)

# update method
# my_dict.update(student_sub_info)
# print(my_dict)

#** kwargs method

# result = {**my_dict, **student_sub_info}
# print(result)   

# classwork create a two empty dictionary one is any football team and another is player in that team
# merge the dictionaries such that final dict. with have a nested dict. with key value pairs.

# football_team = {
#     'team_name' : 'Manchester United',
#     'founded' : 1878,
#     'stadium' : 'Old Trafford',
#     'manager' : 'Erik ten Hag',
#     'coach' : 'Ralf Rangnick',
# }
# players = {
#     'player1' : 'Cristiano Ronaldo',    
#     'height' : '6 ft 2 in',
# },
# {
#     'player2' : 'Bruno Fernandes',
#     'height' : '5 ft 9 in',
# },
# {
#     'player3' : 'Marcus Rashford',
#     'height' : '5 ft 11 in',
# }
# final_dict = {
#     'team_info' : football_team,
#     'players' : players
# }
# # print(final_dict) 
# # print(football_team | {'players': players})  
# print(football_team | players) # this will give error because players is a tuple of dictionaries and we cannot merge a dictionary with a tuple of dictionaries using | operator

# #update method
# football_team.update({'players': players})
# print(football_team)

# # ** kwargs method
# result = {**football_team, **players}
# print(result)

football_team = {
    'name': "football_team",
    'owner': 'abc',
    'coach': 'def',
    'player': None
}

players = {
    'name' : 'Cristiano Ronaldo',
    'height' : '6 ft 2 in',
},
{
    'name' : 'Bruno Fernandes',
    'height' : '5 ft 9 in',
},
{
    'name' : 'Marcus Rashford',
    'height' : '5 ft 11 in',
},


final_dict = {
    'team_info' : football_team,    
    'players' : players
}
print(final_dict)
print(final_dict['team_info']['name']) #accessing team name from final_dict
print(final_dict['players'][0]['name']) #accessing player1 name from final_dict     
# print(final_dict['players'][1]['name']) #accessing player2 name from final_dict 
print(final_dict | {'players': players}) 




