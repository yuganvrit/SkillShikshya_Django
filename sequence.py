# test = [1,2,8,8,5]
# # print(test)

# # print(test[0])


# # last = len(test)

# # print(test[last-1])

# # #slicing
# # print(test[2::])
# # print(tup)

# # print(test[4:2:-1])

# #built in method in list

# #append()

# print(test.append(6))
# print(test)
# test.append(7)
# test.append(7)
# print(test)

# #insert() - adds value at specific index

# test.insert(0,0)
# print(test)

# #remove() -removes the first occurance of value in the list.  

# test.remove(8)
# # test.remove(8)
# print(test)

# #pop() -removes the last element from the list.
# emp = [1,2,3,4,5,7]
# # print(emp.pop())  #last value return garxa.

# print(id(emp))

# emp.pop()
# print(id(emp))

# #index() - return first occurance of value.
# print(test.index(7))

# #count() - it counts the occurance of the value

# print(test.count(7))

# #extend() -combines two list and returns new list.

# test.extend(emp)
# print(test)


# create a list of 10 elements and print the last 5 elements using slicing
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[-5::])

#create a list of 10 elements and print max and min elements in the list

print(max(my_list), min(my_list))

my_list.sort()
print("min", my_list[0], "max", my_list[-1])

#create a list of odd length elements and find the middle elements in the list.
new_list = [1,2,3,4,5,6,7,8,9]
new_list1 = [1,2,3,4,5,6,7]

print(new_list1[len(new_list1)//2])


maximum=[2,1,4,5,3]

print(maximum[::-1])

