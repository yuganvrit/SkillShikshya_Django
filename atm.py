# create a simple atm machine where user can check balance, withdraw money 
# and deposit money
# Simple ATM Machine

# balance = 100000

# choice = int(input("1. withdraw | 2. Check balance | 3. Deposit\n"))

# if choice == 1:
#     wit_amt = int(input("Withdraw amount: "))
#     if wit_amt <= balance:
#         balance -= wit_amt
#         print("Amount deducted successfully!")
#     else:
#         print("Insufficient balance.")

# elif choice == 2:
#     print(f"Your current balance is: {balance}") 

# elif choice == 3:
#     dep_amt = int(input("Enter the amount to deposit: ")) 
#     balance += dep_amt
#     print(f"Deposit successful! New balance: {balance}")


# else:
#     print("Invalid choices selected.") 


# note if we are mentioning int val. then we don,t need to close our opt. with " " but 
# if we are not mentioning int val. then we need to close our opt. with " "(string)
# # or method
# balance = 100000

# while True:
#     choice = (input("\n1. Withdraw | 2. Check balance | 3. Deposit | 4. Exit\n"))

#     if choice == '1':
#         wit_amt = int(input("Withdraw amount: "))
#         if wit_amt <= balance:
#             balance -= wit_amt
#             print(f"Amount deducted successfully! New balance: {balance}")
#         else:
#             print("Insufficient balance.")
    
#     elif choice == '2':
#         print(f"Your current balance is: {balance}")
    
#     elif choice == '3':
#         dep_amt = int(input("Enter the amount to deposit: "))
#         balance += dep_amt
#         print(f"Deposit successful! New balance: {balance}")
    
#     elif choice == '4':
#         print("Thank you for using the ATM!")
#         break
    
#     else:
#         print("Invalid choice selected.")

# another method
balance = 2000  # Initial balance

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: Rs. {balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: Rs. "))
        
        if amount > 0:
            balance += amount
            print(f"Rs. {amount} deposited successfully.")
            print(f"New balance: Rs. {balance}")
        else:
            print("Please enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: Rs. "))
        
        if amount <= balance:
            balance -= amount
            print(f"Rs. {amount} withdrawn successfully.")
            print(f"Remaining balance: Rs. {balance}")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")        