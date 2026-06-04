#create a temperature converter where user can input the temperature in celsius and convert it to fahrenheit and vice versa using simple without using function


temp = input("Enter the temperature in celsius: ")
temp = float(temp)
fahrenheit = (temp * 9/5) + 32
print(f"The temperature in fahrenheit is: {fahrenheit}")

temp = input("Enter the temperature in fahrenheit: ")
temp = float(temp)
celsius = (temp - 32) * 5/9
print(f"The temperature in celsius is: {celsius}")