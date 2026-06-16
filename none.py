#None

# var1 = None
# print(var1)
# print(type(var))

# var2 = []
# print(var2)

# var3 = ""
# print(var3)

# c = {}
# print(type(c))

# d = ()
# print(type(d))

# e = {1,True,'ss'}
# print(type(e))

# print(var1 is None)
# print(var1 == None)
# print(var2 is None)
# print(var1 is var2)
# print(var1 == var2)
# print(var2 == None)
# print(var3 is None)
# print(var3 == None)

# value = None
# if value is None:
#     print("value is None")
#     print("we are learning python")
#     a = 10
#     b = 20
#     print(a + b)

# else:
#     print("value is not None")
#     print("we are not learning python")

# task 
# create a int variable and check it is div. by 5 or not

# var = int(input("enter a number :"))
# if var % 5 == 0:
#     print("var is div. by 5")

# else:
#     print("var is not div. by 5")

# or meth. Create a int variable
# number = int(input("Enter a number: "))

# # Check if divisible by 5
# if number % 5 == 0:
#     print(f"{number} is divisible by 5")
# else:
#     print(f"{number} is not divisible by 5")

# create a dict. and check if the key is present in dict. or not

# dict = {
#     'name': 'samir',
#     'age': 28,
# }

# key = 'name'
# if dict.get(key) is not None:
#     # print('key is present in my dict.')
#     print(f"{key} is in my dict.")

# else:
#     # print('key is not in my dict.')
#     print(f"{key} is not in my dict.")

# create a list of a user with email and pasword as keys
#take user input for email and password
#if user and password matches print login successful else print login failed.

# user_dict = {
#     'email': 'sc5456216@gmail.com',
#     'password': 12345,
# }

# email = True
# password = True

# email_input = input("Enter user email id: ")
# password_input = input("Enter user password: ")

# if email_input == user_dict['email'] and password_input == user_dict['password']:
#     print("login successfull!")

# else:
#     print("login Failed!")

# create a simple atm machine where user can check balance, withdraw money 
# and deposit money
# Simple ATM Machine

# balance = 2000  # Initial balance

# while True:
#     print("\n===== ATM MENU =====")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         print(f"Your current balance is: Rs. {balance}")

#     elif choice == "2":
#         amount = float(input("Enter amount to deposit: Rs. "))
        
#         if amount > 0:
#             balance += amount
#             print(f"Rs. {amount} deposited successfully.")
#             print(f"New balance: Rs. {balance}")
#         else:
#             print("Please enter a valid amount.")

#     elif choice == "3":
#         amount = float(input("Enter amount to withdraw: Rs. "))
        
#         if amount <= balance:
#             balance -= amount
#             print(f"Rs. {amount} withdrawn successfully.")
#             print(f"Remaining balance: Rs. {balance}")
#         else:
#             print("Insufficient balance!")

#     elif choice == "4":
#         print("Thank you for using the ATM.")
#         break

#     else:
#         print("Invalid choice! Please select between 1 and 4.")

# create a temperature checker where user can input the temp
# and check if it's hot, cold or moderate
# temperature = float(input("Enter the temperature (°C): "))

# if temperature >= 30:
#     print("It's Hot 🔥")
# elif temperature >= 15:
#     print("It's Moderate 😊")
# else:
#     print("It's Cold ❄️")


#create a temperature converter where user can
#input the temperature in celsius and convert it to fahrenheit and vice versa    

# Temperature Converter

# print("Temperature Converter")
# print("1. Celsius to Fahrenheit")
# print("2. Fahrenheit to Celsius")

# choice = input("Enter your choice (1 or 2): ")

# if choice == "1":
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C = {fahrenheit:.2f}°F")

# elif choice == "2":
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print(f"{fahrenheit}°F = {celsius:.2f}°C")

# else:
#     print("Invalid choice! Please enter 1 or 2.") 








