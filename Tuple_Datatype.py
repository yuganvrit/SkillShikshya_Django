# this_tuple=("apple", "banana", "cherry")
# print(id(this_tuple))
# this_tuple=(1,2,3,4)
# print(id(this_tuple))

# Tuple = (1,2,3,4)
# print(type(Tuple))


# tuple = (1,)
# print(type(tuple))

# tuple=1,2,3,4
# print(type(tuple))

# print(Tuple[:1])
# print(Tuple[-1:])

##unpacking of tuple

# tuple = (1,2,3)
# a,b,c = tuple
# print(a)
# print(b)
# print(c)

# a,*b = tuple
# print(a)
# print(b)

##Packing of tuple]

# a = 1
# b = 2
# tuple = a,b
# print(tuple)


## Take input from user and create a tuple of 5 element and print the  tuple
# user = input("Enter the elements: ")
# tuple = user
# print("Tuple: ", tuple)

## take input from the user single time only and take a number seperated by comma and print every single element from input

# user = tuple(input("Enter the element: "))
# print(user)
# a,b,c,d,e= user
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# next_tuple = (1,2,3,4,5,5,6,1)
# next_tuple.count(5)
# print(next_tuple.index(5))

##Nested tuple

# nested_tuple = (1,2,3,(4,5,6),7)
# print(nested_tuple[3][1])


##mutable Tuple
# mutable_tuple = (1,2,3,[4,5,6],7)
# print(mutable_tuple)

# mutable_tuple = (1,2,[3,4],5)
# print(mutable_tuple[2].insert(1,5))
# print(mutable_tuple)

# mutable_tuple = (1,2,"santos",5)
# print(mutable_tuple[2].append("h"))

# three_level_tuple = (1,2,(3,4,(5,6)),7)
# print(three_level_tuple[2][2][1])

# m_tuple = (1,2, "Santos", 5)

# m_list = list(m_tuple)
# name = m_list[2]
# name = name + "h"
# m_list[2] = name
# m_tuple = tuple(m_list)
# print(m_tuple)
