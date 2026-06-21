# square = {x: x**2 for x in range(11)}
# print(square)


# task
# suppose there is dict of st marks in inside a list 

student_dict = [
    {
    'name': "Sahil",
    "science": 70,
    "math": 97
    },
    {
    'name': "Ram",
    "science": 80,
    "math": 90
    },
]

new_list = [ val["math"] + val["math"] for val in student_dict if type(val)=='int']

print(new_list)


# new_dict = {{ ele: ele for ele in element.values()} for element in range(student_dict)}

# for x in student_dict:
#     print(x)


# st1 = {
#     'name': "Sahil",
#     "science": 80,
#     "math": 99
#     }
# print(st1["science"])
# print(st1["math"])




nums = [
    [1, 2, 3, 4], [3, 2, 3, 1, 3]
]

new_num = {i: sum(num) for i, num in enumerate(nums)}
print(new_num)