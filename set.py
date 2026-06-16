# numbers = {1, 2, 3, 3, 4, 5}
# print(numbers)
# print(type(numbers))

# numbers[0] #gives error because set is unordered and unindexed  
# numbers.add(6)
# print(numbers)   

#create a empty set
#start adding elements to the set
# check how duplicate elements adding is prevented and what is the behavior
#try to do indexing and find out the output
#prove set is mutable using memory id concept

# empty_set = set()
# print(empty_set)
# print(type(empty_set))
# empty_set.add(1)
# print(empty_set)
# empty_set.add(2)    
# print(empty_set)
# empty_set.add(2)
# print(empty_set)
# # print(empty_set[0]) #gives error because set is unordered and unindexed
# print(id(empty_set))
# empty_set.add(3)
# print(id(empty_set))

# create a list which contains some duplicate elements
#remove all duplicate elements from that list

# lst = [1, 2, 3, 3, 4, 5]
# unique_list = list(set(lst))
# print(unique_list)

# set method
# first_set = {1, 2, 3, 4, 5}
# second_set = {4, 5, 6, 7, 8}

# print(first_set.union(second_set)) #union of two sets
# print(first_set.intersection(second_set)) #intersection of two sets 

# print(first_set | second_set) #union of two sets
# print(first_set & second_set) #intersection of two sets 
# print(first_set - second_set) #difference of two sets
# print(second_set - first_set) #difference of two sets   
# # print(first_set ^ second_set) #symmetric difference of two sets
# print(first_set.symmetric_difference(second_set)) #symmetric difference of two sets

# classwork create two lists and find out those elements which exist in first list only
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

list1_set = set(lst1)
list2_set = set(lst2)
unique_to_list1 = list1_set - list2_set
unique_to_list1 = list(unique_to_list1)
print(unique_to_list1)  


