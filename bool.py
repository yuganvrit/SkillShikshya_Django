# #check 0.1 + 0.2 == 0.3 (True or False)

print(0.1 + 0.2 == 0.3)
# # Gives false becz of the way floating point numbers are represented in binary, it cannot represent 0.1 and 0.2 exactly, so it gives a result that is very close to 0.3 but not exactly 0.3
print(0.1 + 0.2)


# #But 
print(round(0.1 + 0.2 , 10)) #output gives 0.3 becz it will round to 10 decimal places 
# #but again if 
print(round(0.1 + 0.2))
# # output gives zero becz it will round to nearest integer i.e 0.0 

print(0.4 + 0.4 == 0.8)
print(0.4 + 0.4)
# Gives true becz the rounding errors are cancel out in specific case.

#but case
print(round(0.4 +0.4 , 10))
# output gives 0.8 becz it will round to 10 decimal places

#and
print(round(0.4 +0.4))

# and for 
print(round(0.3+0.2))

print(0.25 + 0.25 == 0.5)










