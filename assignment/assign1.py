#find the second largst number in list
# lst = [1,2,9,3,4,5,8]

# largest = lst[0]
# second_largest = lst[1]

# for i in lst:
#     if i > largest:
#         largest = i
        

# #2nd way to do.
# lst.sort()
# print(lst[-2])

# maximum = max(lst)
# lst.remove(maximum)
# larg = lst[0]


# for i in lst:
#     # if i != larg:
#         if i > larg:
#             larg = i
# maximum = larg

# larg = lst[0]
# for i in lst:
#     if i != maximum:
#         if i > larg:
#             larg = i
# supermax  = larg

# print(maximum)

# # lst.remove(maximum)
# print(supermax)



#2. Check if two strings are ANAGRAMS(eg. 'listen' and 'silent')

# first = input("Enter the first string: ")
# second = input("Enter the secodn string: ")
first = ('good')
second = ('dodg')


if len(first) == len(second):
    anagram = 0
    for i in first:
        if first.count(i) == second.count(i):
        # for j in second:
        #     if first.count(i) == second.count(j):
                anagram += 1
        #         break
            

if (anagram == len(first)):
    print("This is a anagram word!!!")
else:
    print("This is not an anagram word")