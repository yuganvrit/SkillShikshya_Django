# list = [1,2,3]
# engine = iter(list)

# print(dir(list)) # to check u can use for loop or not. also look iter function there.

# print(next(engine))
# print(next(engine))
# print(next(engine))

# iteration using for loop

grades = ["a", "b", "c"]  # Iterable

for grade in grades:      # Automatically creates iterator & iterates
    print(grades)


# wap for loop that prints each name with a greetings: "Hello, aloce"
# wap for loop that counts how many names have more than 5 letters. print the count.

# name = ["Samir", "alice", "ram"]


# for n in (name):
#     # print('Hello ' + n)
#     print(f"Hello  {n}")

# wap for loop that counts how many names have more than 5 letters. print the count.

# names = ["Samir", "alice", "ram", "Sandeep", "Sandhya", "Raju", "Sushmita"]

# count = 0

# for n in names:
#     name_length = len(n)
#     if name_length > 5:
#         count +=1
#         print(f"{n} has {name_length} letters")  # Optional: show which names qualify

# print(f"\nTotal names with more than 5 letters: {count}")

names = ["Samir", "alice", "ram", "Jonathan", "Elizabeth", "Bob", "Alexander"]

count = 0

for name in names:
    if len(name) > 5:
        count += 1  

print(f"Count: {count}")

# names = ["Samir", "alice", "ram", "Jonathan", "Elizabeth"]

# count = 0
# for name in names:
#     count = count + (len(name) > 5)  # This adds True (1) or False (0)

# print(f"Count: {count}")





