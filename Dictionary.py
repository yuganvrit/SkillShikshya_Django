# # my_dict = {
# #     "name" : "Prince",
# #     "age" : 24,
# #     "city" : "Kathmandu",
# #     "college" : "HCOE"
# #     }
# # # print(my_dict)
# # # print(type(my_dict))
# # print(my_dict["age"])
# # my_dict["gender"] = "male"
# # print(my_dict["gender"])
# # my_dict["age"] = 25
# # del my_dict["gender"]
# # print(my_dict.get("name"))

# # # print(my_dict)

# # #update the  value pair in dictionary
# # my_dict["name"] = "Raghabendra"
# # print(my_dict)


# # ## Create a empty dictionary
# # empty_dict ={}
# # print(type(empty_dict))

# # ## Fetches the keys from the dictionary
# # print(my_dict.keys())
# # print(my_dict.values())


# # ## fetches pair as item
# # print(my_dict.items())

# # ## Pop method of dictionary
# # my_dict.pop("city")
# # print(my_dict)

# # ## Pop item method of dictionary
# # print(my_dict.popitem())
# # print(my_dict)

# ##merging to dictionaries
# # my_dict2 ={
# #     'name':'Raghabendra', #overwrite hunxa jun chai merge garxau
# #     'hobby' : 'coding',
# #     'language' : 'python'
# # }
# # # | method
# # # print(my_dict | my_dict2)

# # ##update method
# # my_dict.update(my_dict2)
# # print(my_dict)


# # ## * kwarge method
# # result = {**my_dict, **my_dict2}
# # print(result)


# # ## classwork create a two empty dictionary one is any football team and another is players in that team 
# # ## merge the dictionary such that final dictionary with have  a nested dictionary eith key players

# football = {
#     'name': 'Real Madrid',
#     'owner' : 'Florentino Perez',
#     'coach': 'Jose Mourinho',
#     'player' : None

# }

# players =[{
#         'name' : 'Mbappe',
#         'height' : 6.3,
#     },
# {
#         'name' : 'Vinicius Jr.',
#         'height': 5.11
#     },
# {
#         'name' : 'Arda Guler',
#         'height': 5.9
#     }
# ]


# print(football | {'player': players})


