# Create a empty set 
#start adding element in set
#check how duplicate element addimg is prevented and what is the behaviour 
#try to do indexing and fing out the output
# prove set is mutable using memory id concept


# empty_set =set()
# print(empty_set)
# empty_set.add(1)
# empty_set.add(2)
# empty_set.add(3)
# empty_set.add(4)
# empty_set.add(5)

# print(empty_set)

# empty_set.add(5)
# print(empty_set)
# print(id(empty_set))
# empty_set.add(1)
# print(id(empty_set))

# # create a list which is contain some duplicate elements
# # remove all the duplicate element from that list

# my_list = [1,1,2,3,4,4,5,6]
# unique_list = list(set(my_list))
# print(unique_list)


# first_set = {1,2,3,4,5}
# second_set = {4,5,6,7,8}
# print(first_set | second_set) #union
# print(first_set & second_set) #intersection
# print(first_set - second_set) #difference
# print(first_set ^ second_set) #symmetric difference




## classwork create a two list and find out those element which exist in first list only

# first_list = [1,2,3,4,5]
# second_list = [4,5,6,7,8]
# set_first = set(first_list)
# set_second = set(second_list)

# existing_list = list(set_first - set_second)
# print(existing_list)