#brother of dictionary with onlyy keys.
# create emp set add some elements. see how duplicates are handled. add elem, try index, try remove

emp_set= set()

print(id(emp_set))

emp_set.add(1)
emp_set.add(2)
emp_set.add(3)
emp_set.add(3)

print(id(emp_set))

emp_set.add(5)
emp_set.add(7)

print(emp_set)
# print(emp_set[1])

emp_set.remove(1)

print(id(emp_set))

#create a list which contains some duplicate elements
lis = [1,1,1,2,3,4,5,5,43,6,7]

#return a fresh list removing all the duplicates.
lis = list(set(lis))
print(lis)

#union, intersection and difference, symmetric difference

a = {1,2,3,4,5}
b = {4,5,6,7}

# print(a | b)
# print(a & b)
# print(a - b)

# print(a.symmetric_difference(b)) ( U - ( a U b))

#c/w create two lists and find out those elements which exist in first list only
a = [1,2,3,4,5]
b = [4,5,6,7]

c = set(a)
d = set(b)

print(set(c -d) )