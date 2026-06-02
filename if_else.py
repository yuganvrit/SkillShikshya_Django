# #task 
# #create a int variable and check if it is divisible by 5 or not

# var = 0

# if(var % 5 == 0):
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")

# #create dict and check if the key is present in dict or not

# dictionary = {'name': 'Santosh', 'age':5, 'city': 'ktm'}

# key = 'name'

# if(dictionary.get(key) is not None):
#     print("The key is present")
# else:
#     print("The key is not prsent")

# student = True
# has_identity_card = False

# if(student and has_identity_card):
#     print("Student has identity card and can access the library")
# else:
#     print("Student doesn't have identity card and cannot access the library")


# #create a dict of a  user which contain email and password as keys. if user and password matches print login successfull else print login failed


# user = {'user': 'Santosh', 'password': '1234'}

# uname = input("Enther the username: ")
# pwd = input("Enter the pwd: ")

# if(uname == user['user'] and pwd == user['password']):
#     print("login successful")
# else:
#     print("login failed! Try again!!")

#create a simple atm machine where user can check blc, withdraw money and deposit

balance = 10000

opt = int(input("1. Withdraw 2.Check Balance 3.Deposit"))
if(opt == 1):
    wit_amt = int(input("Enter the amt to withdraw: "))
    if(wit_amt <= balance):
        balance -= wit_amt
        print("Your amount is deducted successfully")
    else:
        print("You don't have enough blc.")

elif opt == 2:
    print("You currently have balance: ", balance)

elif opt == 3:
    dep_amt = int(input("Enter the amt to deposit: "))
    balance += dep_amt
else:
    print("You entered default option")



#create a temperature checker where user can input the temp and check if it's hot, cocld or moderate

temp = int(input("Enter the temperature(Celcius): "))

if (temp >= 21 and temp <=29):
    print("The temperature is moderate")
elif(temp <= 20):
    print("The temperature is cold")
elif (temp >= 30 ):
    print("The temp is hot.")
else:
    print("invalid input.....")