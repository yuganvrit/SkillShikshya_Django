#range data type

#range can be indexed, sliced, 

first_five_number = range(5)
print(type(first_five_number))
print(first_five_number[0])

# first_five_number[0] = 6
print(first_five_number)

multiple_of_4 = list(range(4,41,2))

print(multiple_of_4[::2])


multiple_of_8 = list(range(8,81,2))
print(multiple_of_8)
print(multiple_of_8[::4])