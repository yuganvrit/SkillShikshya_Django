# first_five_numbers = range(5)
# print(list(first_five_numbers))

# print(type(first_five_numbers))
# print(first_five_numbers)
# print(first_five_numbers[1])#we can indexing in range
# print(first_five_numbers[:3]) # we can slicing in range
# print(first_five_numbers[-1]) # we can negative indexing in range
# print(first_five_numbers[::2]) # we can step in range

#multiples of 5

multiples_of_5 = range(5,51,1)
print(list(multiples_of_5))
print(list(multiples_of_5[::5]))

#direct mthod to calc. multi. of 5
multiples_of_5_direct = range(5, 51, 5)
print(list(multiples_of_5_direct))  


#multiples of 12

multiples_of_12 = range(12,121,2)
print(list(multiples_of_12))    
print(list(multiples_of_12[::6]))

#direct method to calc. multi. of 12
multiples_of_12_direct = range(12, 121, 12)
print(list(multiples_of_12_direct))



