x = 2
y = 3
z = x + y
print(f'sum of {x} and {y} is: {z}')

#Python data types:
#String: Text Data, Eg: "Hello", Python Keyword: str
#Integer: Whole Numbers, Eg: 10, Python Keyword: int
#Float: Decimal Numbers, Eg: 3.14, Python Keyword: float
#Boolean: Conditional, Eg: True/False, Python Keyword: bool

name = "Sakshyam"
print(id(name))
city = "Kathmandu"

print(f'My name is {name}. I live in {city}.')
name = name + ' Shahi'
print (name)
# print(id(name))

#checking if int and float are mutable or immutable:

#int
a = 5
print(id(a))
a = a + 2
print(id(a))

#float
b = 2.1
print(id(b))
b = b + 4
print(id(b))

#Operators:

c = 10
d = 5
print(f'{c} - {d} = {c-d}')
print(f'{c} + {d} = {c+d}')
print(f'{c} x {d} = {c*d}')
print(f'{c} / {d} = {c/d}')
print(f'{c} // {d} = {c//d}')
print(f'{c} % {d} = {c%d}')
print(f'{c} ** {d} = {c**d}')

var1 = "Sakshyam"
var2 = 10
var3 = 100.10
var4 = True
print(id(var4))
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
var4 = False
print(id(var4))

#interactive prgm

name = input("Enter Your Name: ")
print(f'Your name is {name}')

#Type Conversion

value = '10'
int_value = int(value)
print(int_value)
print(type(int_value))

value2 = int(100)
strvalue = str(value2)
print(strvalue)
print(type(strvalue))

#task: take inputs from user (at least 2) and print outputs after doing a.operator.

val1 = int(input('Enter 1st Number: '))
val2 = int(input('Enter 2nd Number: '))
print(f'{val1} + {val2} = {val1 + val2}')
print(f'{val1} - {val2} = {val1 - val2}')
print(f'{val1} * {val2} = {val1 * val2}')
print(f'{val1} / {val2} = {val1 / val2}')
