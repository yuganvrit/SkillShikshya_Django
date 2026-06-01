emp_set = set()

#Adding elements
emp_set.add(1)
emp_set.add(2)
emp_set.add(3)
emp_set.add(4)
emp_set.add(5)

print(emp_set)

print(id(emp_set))

#Remove
emp_set.remove(3)
print(emp_set)

#duplication
emp_set.add(1)
print(emp_set)

# #Indexing
# print(emp_set[0])

print(id(emp_set))

#Task>>>>> Create a list which contains some duplicate elements, remove all duplicate elements from that list

example = [1, 1, 1, 1, 2, 3]
output = list(set(example))
print(output)

first_set = {1,2,3,4}
second_set = {3,4,5,6}

print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)
print(first_set.symmetric_difference(second_set))

#Task>>>>> Create two list and find out those elements which exist in first list only

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
diff = set1 - set2
print(list(diff))

#What is RAG, diff between vectorless rag and traditional rag. what is vector embedding
