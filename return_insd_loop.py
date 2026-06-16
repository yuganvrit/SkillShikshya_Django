# # return inside loop
# # 🔴 If inside loop:
# # return happens early → function stops immediately
# # here we call var. outside function
# def sum_natural_numbers(*args):
#     total = 0
#     for element in args:
#         total += element
#         return total   

# result = sum_natural_numbers(1,2,3,4,5)
# print(result) # output-> 1

# # now calling var. inside function
# def sum_natural_numbers(*args):
#     for element in args:
#            total = 0
#            total += element
#     return total   

# result = sum_natural_numbers(1,2,3,4,5)
# print(result) # output-> 5

# # return outside loop
# #🟢 If outside loop:
# # loop completes first → then return happens

# # calling var. outside function
# def sum_natural_numbers(*args):
#     total = 0
#     for element in args:
#         total += element
#     return total   

# result = sum_natural_numbers(1,2,3,4,5)
# print(result) # output-> 15

# #calling var. inside function
# def sum_natural_numbers(*args):
   
#     for element in args:
#          total = 0
#          total += element
#          return total   

# result = sum_natural_numbers(1,2,3,4,5)
# print(result) # output-> 1

for element in (1,2,3):
    total = 0
    total += element
    print(total) # output in the form of 0+1,0+2,0+3(1 2 3)

total = 0
for element in (1,2,3):
    total += element
    print(total) # output-> 1 3 6




