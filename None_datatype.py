# a =  None
# print(type(a))


# # a = []
# # print(type(a))

# b={}
# print(type(b))

# c = ''
# print(type(c))

# # print(a is None)  ## is le identity check garxa or memory address check garxa
# # print(b is None)
# # print(c is None)


# print(a == b)  ## == le value check garxa

# print(a is b)

# ## None is sensitive to data type ##



# value = None
# print(value is None)
# print(value == 0)
# print(value is not None)

# ## Conditions (if/elif/else)

# age = 18 
# if age >= 18:
#     print("You are eligible to vote.") 

# value = None
# if value is None:
#     print("Value is None.")
#     print('we are learning about the condition in python')
#     a = 10
#     b = 20
#     print(a+b)
# else:
#     print("Value is not None.")
#     print('we are learning about the condition in python')


## Task 
## Create a int variable and check if it divisible by 5 or not


# value =int(input("Enter a number: "))
# if value % 5 == 0:
#     print("value is divisible by 5")
# else:
#     print("value is not divisible by 5")


## Create  a dict and check if key is present  in dict or not
# my_dict = None
# my_dict = {
#     'name': 'Raghabendra',
#     'age' : 24,
#     'city' : 'Kathmandu'
# }
# if my_dict.get('name') is not None:
#     print("Key is present in the dictionary.")
# else:
#     print("Key is not present in the dictionary.")


# student = True
# has_identity_card = False

# if student and has_identity_card:
#     print("Student has an identity card and can access the library.")
# else:
#     print("Student does not have an identity card and cannot access the library.")


## create a dict of a  user with email and password as keys
## take a user input for email and password 
## if user and password matches print login successful else print login failed


# user_dict = {
#     'email' : 'abc@gmail.com',
#     'password' : '12345'
# }

# email_input = input('enter your email: ')
# password_input = input('enter your password: ')

# if email_input == user_dict['email'] and password_input == user_dict['password']:

#     print("Login successful")
# else:
#     print("Login failed")



## create a simple atm machine where user can check balance , withdraw money and deposite money

# balance = 10000
 
# user_input = int(input("enter a choice: 1. Check balance 2.withdraw Money 3. Deposite Money: "))
# if user_input == 1:
#     print(f"your balance is : {balance}")

# elif user_input ==2:
#     withdraw = int(input("Enter the amount to withdraw: "))
#     if withdraw <= balance:
#         balance -= withdraw
#         print(f"withdraw successfully.")
#     else:
#         print(f"insufficent balance")

# elif user_input == 3:
#     deposite = int(input("Enter the amount to be deposite: "))
#     balance += deposite
#     print(f"Deposited successfully and your balalnce is:{balance}")

# else:
#     print(f"invalid choice")


# marks = 95
# if marks >= 90:
#     print("Grade A")
# elif marks >=80:
#     print("Grade B")
# elif marks >=70:
#     print("Grade C")
# elif marks >=60:
#     print("Grade D")

# else:
#     print("Grade E")






