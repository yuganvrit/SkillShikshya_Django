#Day 3: Dictionary, Set, None and Conditional Statement

student = {
    'Name' : 'Sakshyam',
    'College' : 'HCK',
    'Age' : 2,
    'City' : 'Kathmandu'
}

#Accessing Keys
print(student['Name'])
#Alt: Using .get() won't break the code if error occurs.
print(student.get('Name'))

#Adding New Key:Value Pair
student["Country"] = "Nepal"
print(student)

#Updating existing value
student['Age'] = 22
print(student)

#Deleing 
del student["Country"]
print(student)

#create an empty dict
empty_dict = {}
print(type(empty_dict))

#Fetching the keys from a dict
print(student.keys())
print(student.values())

#Fetch pair as item
print(student.items())

#Pop method in dict
print(student.pop('Age'))
print(student)

#popitem method in dict
print(student.popitem())
print(student)

#>>>merging two dict

student_sub_info = {
    'Name': 'Testname',
    'grade': 12,
    'address': 'Kathmandu'
}

# | method
print(student | student_sub_info)

#Update Method
student.update(student_sub_info)
print(student)

#Kwargs method
result = {**student, **student_sub_info}
print(result)

#Task>>>> Create two empty dictionary 
player = [
    {
    "Player Name": "Ronaldo ko bau",
    "Player Height": 160,
    "Player Rating": 90
    },
    {
    "Player Name": "Messi ko bau",
    "Player Height": 120,
    "Player Rating": 88
    }
]
team = {
    "Club Name": "Nepal FC",
    "Coach": "Abcd123",
    "Owner": "ANFA"
}
team['Players'] = player
print(team)

#Shallow Copy
copy_dict = team.copy()
print(copy_dict)
#clear method
team.clear()
print(team)

print(len(student))

