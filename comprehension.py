# take a list of string and use list comprehension to uppercase each element of list

lst = ['ram', 'hari', 'sita', 'geeta']

upper = [x.upper() for x in lst if len(x) < 5]
print(upper)



#dictionary comprehension.

#suppose there is a dictionary of students marks inside a list:

lst =[
    {
        'name':'xyz',
        'science':80,
        'math':99
    },
    {
        'name':'abc',
        'science':80,
        'math':99
    },
    {
        'name':'xysz',
        'science':80,
        'math':99
    },
    {
        'name':'xsyz',
        'science':80,
        'math':99
    },
]


source = [
    [1,2,3,4], [5,6,7,8],[89,23,12]
]

maxValues = { i:max(v) for i, v in enumerate(source) }
print(maxValues)