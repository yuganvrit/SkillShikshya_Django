# while True:
#     print("Hello")

# 3. Game loop
# playing = True
# score = 11
# while playing:
#     print(f"Score: {score}")
#     answer = input("Continue? (y/n): ")
#     if answer == 'n':
#         playing = False
#     else:
#         score += 10

#create a list called grades with five numbers .
# Then:

# grades = ["a", "b", "c", "d"] # iterable -> Collections of data

# engine = grades.__iter__()# iterator -> remember positions(pointer/mechanism)
# # engine = iter(grades)

# print(next(engine))
# print(next(engine)) # Iteration -> Getting item one by one (i.e. in process)
# print(next(engine))
# print(next(engine))
# print(next(engine))
# print(next(engine))
# grades = ["a", "b", "c"]  # Iterable

# for grade in grades:      # Automatically creates iterator & iterates
#     print(grades)

# Is vs in 

# in -> checks membership(i.e. value exists)

print(2 in [1,2,3]) # It gives True bcz 2 is members of this list
print(5 in (1,2,3)) # it gives False bcz 5 is not members of this list

# is -> checks identity(i.e. memory location of the var.)

x = [1,2,3]
y = x
z = [1,2,3]


print(x is y)
print(x is z)
print(x == z)



