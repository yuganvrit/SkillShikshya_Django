# student = {
#     "name":"Santosh Bohara",
#     "college":"Kathmandu Bernhardt College",
#     "city":"ktm",
#     "age":23
# }
# print(type(student))

# print(student["name"])
# student["color"]="blue"
# print(student)

# del student["age"]

# print(student)

# print(student.get("city"))

# #access method in dict:
# print(student['name'])


# #update key value pair in dict
# student["name"] = "Samir"
# print(student)

# #get keys
# print(student.keys())

# #get  values
# print(student.values())


# #fetch pair as item
# print(student.items()) # return as tuple for each key value

# #remove item from dict.
# student.pop("city")
# print(student)


# #popitem
# student.popitem()  # removes last item from dict.


# #merge dicts. | use this sign..
# student2 = {
#     "name":"Santosh Bohara",
#     "course":"BCA",
#     "greet":"hello"
# }

# print(student | student2)

# #update is used to merge two dicts.
# student.update(student2)
# print(student)

# #**kwargs

# result = {**student, **student2}
# print(result)



#cw: create a two empty dictionary one is any football team and another is players in that team. merge the dictionary such that final dictionary will have a nested dit with key players

team = {
    'name':"FCN",
    'coach':"hello",
    "owner": "Balen Sarkar"
}

player=[
    {
    "name":"player1",
    "height":5.6
    },
    {
    "name":"player1",
    "height":5.6
    },
    {
    "name":"player1",
    "height":5.6
    },
    {
    "name":"player1",
    "height":5.6
    },
    ]

team['player'] = player
print(team)

# #clear the dict
# team.clear()

#copy the dict with another
shallow_copy = team.copy()
print(shallow_copy)

#length returns no. of key->value pairs.
print(len(team))