first_name = input("Enter First name of the user: ")
last_name = input("Enter last name of the user: ")
age = input("Enter user age: ")
salary = input("Enter user salary: ")
user_job = input("Enter user job: ")

concatenate = first_name + " " + last_name + " " + age + " " + salary + " " + user_job
print(concatenate)

# Checking the price rate
price = int(input("Enter total price: "))
rate = int(input("Enter total rate: "))


OneGrocery_price = price / rate
print(f"The price of One grocery is {OneGrocery_price}")
print(type(OneGrocery_price))

# Checking the total balance
income = 2000
expenses = 400

incomeminus_exp = income - expenses

print(f"Total income is {income}")
print(f"Total expenses is {expenses}")
print(f"Total Balance is {incomeminus_exp}")

