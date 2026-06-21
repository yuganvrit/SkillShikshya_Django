# list comprehension 

# square numbers
square = [x**2 for x in range(6) if x > 0]
print(square)


# try for prime numbers

# [expression loop condition]
# (expression loop condition)
# {expression loop condition}    sets
# [expression loop condition]


# taking a list of string and use list comprehension to upper case each element in the list
name = "sahil"
upper = [char.upper() for char in name ]
print(upper)

# filter out the string more than 5 words
name_list = ["Sahil", "fhejifhe", "ram"]

selected = [name for name in name_list if len(name) <= 5]
print(selected)