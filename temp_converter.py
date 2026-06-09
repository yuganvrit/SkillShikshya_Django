#create a temperature converter where user can input the temperature in celsius 
#and convert it to fahrenheit and vice versa

#temperature converter
opt = 1
print("Celsius to fahrenheit")
opt = 2
print("fahrenheit to celsius")

opt = float(input("Enter your option (1 or 2): "))

if opt == 1:
    celsius = float(input("Enter temp. in celsius: "))
    fahrenheit = (celsius * 9/5 + 32)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")    

elif opt == 2:
    fahrenheit = float(input("Enter temp. in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("Invalid choice! please enter 1 or 2.")





