# single_quote_name = 'Santosh'
# double_quote_name = "Santosh"

# print(single_quote_name)
# print(double_quote_name)

# #string concatenation
# full_name = single_quote_name +" " + " Bohara"
# print(full_name)
# print(id(full_name)) # this will print the memory address of the string object.
# full_name = full_name + " is a student"
# print(id(full_name)) # this will print a different memory address because strings are immutable in python. when we concatenate, it creates a new string object in memory.


# num =5
# print(id(num)) # this will print the memory address of the integer object.
# num = num + 1
# print(id(num)) # this will print a different memory address because integers are also immutable in python


# number = 12.9
# print(id(number))

# number = number+11
# print(id(number))

# c = 4
# d=3

# print(f"{c} + {d} = {c+d}")
# print(f"{c} - {d} = {c-d}")
# print(f"{c} * {d} = {c*d}")
# print(f"{c} / {d} = {c/d}")
# print(f"{c} % {d} = {c%d}")
# print(f"{c} // {d} = {c//d}")
# print(f"{c} ** {d} = {c**d}")

# var1 = "Santosh"
# var2 = 12
# var3 = 12.9
# var4 = True
# print(id(var4))
# var4 = False
# print(id(var4))

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))

# ent = input("Enter your name: ")
# first = int(input("Enter your first number"))
# second = int(input("Enter your second number"))

# print("The number is ", first+second)


# value = str(100)
# print(type(value))

#task 1

firstnum= int(input("Enter the first number: "))
secondnum= int(input("Enter the second number: "))

print(f"The sum of {firstnum} and {secondnum}: ", firstnum + secondnum)
print(f"The subtraction of {firstnum} and {secondnum}: ", firstnum - secondnum)
print(f"The division of {firstnum} and {secondnum}: ", firstnum / secondnum)
print(f"The multiplication of {firstnum} and {secondnum}: ", firstnum * secondnum)
print(f"The floor division of {firstnum} and {secondnum}: ", firstnum // secondnum)
print(f"The modulo of {firstnum} and {secondnum}: ", firstnum % secondnum)


#task 2

fname = input("Enter the first name: ")
lname = input("Enter the last name: ")

print(f"My name is {fname + " "+lname }")