# #for loop

# items = ["bags", "books", "pens", "erasers"]

# for name in items:
#     print(f"items", {name})

# #next eg:

# friends = ["Sabin", "Sandip", "Randip", "Hiran"]

# for name in friends:
#     print(f"Hello", {name})

# for person in friends:
#     print(f"{person} is here but {person} mind is there.")

#range(5). It prints from 0-4
for i in range(5):
    print(i)

#range(1,6). here start is included but stop is not included 
for i in range(1,6):
    print(i)

#range(1,11). It is used for multiplication table.
for i in range(1,11):
    print(f"2 * {i} = {2 * i}")


#range(dtart,stop,skip):
#range(0,11,2): Output= 0,2,4,6,8,10 becz it skips after every 2 num. becz of given condN.
for i in range(0, 11, 2):
    print(i, end=" ")

print()

#printing odd numbers

for i in range(1, 13 ,2):
    print(i, end=" ")
print()

#count by 10s

for i in range(10, 101, 10):
    print(i, end=" ")
print()  

for i in range(10, 101, 10):
    print(f"5 * {i} = {5 * i}")

#counting down
for i  in range(10, 0, -1):
      print(f"T minus {i}...")
print("Liftoff! 🚀")    
    #   print(i, end=" ")
# print()










