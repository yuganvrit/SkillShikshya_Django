# #Task 1: Create an int variable and check if it is divisible by 5 or not

# x = 12
# if x % 5 == 0:
#     print("Perfect")
# else:
#     print("SOrrryyy") 

# #Task 2: 
# dictt = {
#     'fruits': 'Apple',
#     'color': 'Red'
# }
# if (dictt.get('fruit') is not None):
#     print("Xaaaa")
# else:
#     print('Xainaaaaa')


# student = True
# has_id_card = False

# if student and has_id_card:
#     print("Permission Granted")
# else:
#     print("Access Denied")

# #Task 3: Create a dictionary of an user with email and password as keys and take user input for email and password. if user and password matches print login sucessful else print failed

# users = {
#     'email' : 'shahi.reson17@gmail.com',
#     'password' : 'Abcd1234'
# }
# user_email = input("Enter Email: ")
# user_pass = input('Enter Password: ')

# if (user_email == users['email'] and user_pass == users['password']):
#     print('Login Sucessful')
# else:
#     print("Failed")

#Task 4: create a simple ATM machine where user can check balance, withdraw money and deposit
# total_balance = 1000
# balance = 1
# withdraw = 2
# deposit = 3

# user_inp = int(input("Press 1 to check balance, 2 to withdraw and 3 to deposit: "))

# if(user_inp == balance):
#     print(f"Your balance is {total_balance}")

# elif(user_inp == withdraw):
#     blc_inp = int(input('Kati Jhikxas?: '))
#     if(blc_inp <= total_balance):
#         total_balance -= blc_inp
#         print("Paisa Niskyoooo")
#     else:
#         print("Aaukaattt!!")
    
# elif(user_inp == deposit):
#     dep_inp = int(input("Kati Halxas?: "))
# else:
#     print("Wrong INput")


#Task 5: Check a temp

moderate_temp = 21
user_temp = int(input("Enter Temperature: "))

if user_temp > moderate_temp:
    print("To Hot!")
elif user_temp < moderate_temp:
    print("To Cold!")
else:
    print("Its Moderate")