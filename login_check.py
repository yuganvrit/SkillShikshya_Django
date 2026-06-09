# # # create a list of a user with email and pasword as keys
# # #take user input for email and password
# # #if user and password matches print login successful else print login failed.

# # # Create a list of users with email and password as keys
# # users = [
# #     {"email": "john@example.com", "password": "john123"},
# #     {"email": "sarah@example.com", "password": "sarah456"},
# #     {"email": "mike@example.com", "password": "mike789"}
# # ]

# # # Take user input for email and password
# # email = input("Enter your email: ")
# # password = input("Enter your password: ")

# # # Check if user and password matches
# # login_successful = False

# # for user in users:
# #     if user["email"] == email and user["password"] == password:
# #         login_successful = True
# #         break

# # # Print result
# # if login_successful:
# #     print("✓ Login successful!")
# # else:
# #     print("✗ Login failed! Invalid email or password")

# # Imagine you're a security guard checking IDs

# # Start with assumption: Person is NOT allowed in
# allowed = False  # ← Starting point

# # Check each person
# people_checked = 0

# person1 = {"name": "John", "id": "A123"}
# person2 = {"name": "Sarah", "id": "B456"}  
# person3 = {"name": "Mike", "id": "C789"}

# for person in [person1, person2, person3]:
#     if person["id"] == "B456":  # Looking for Sarah
#         allowed = True  # ← Change to True ONLY when found
#         print(f"Found {person['name']}! Access granted")
#         break

# if allowed:
#     print("✅ Person allowed inside")
# else:
#     print("❌ Person denied access")

# Without setting False val.
users = [
    {"email": "john@example.com", "password": "john123"},
    {"email": "sarah@example.com", "password": "sarah456"},
    {"email": "mike@example.com", "password": "mike789"}
]

# # # Take user input for email and password
email = input("Enter your email: ")
password = input("Enter your password: ")

for user in users:
    if user["email"] == email and user["password"] == password:
        login_successful = True  # ERROR! login_successful not defined yet

if login_successful:  # ERROR! variable doesn't exist
    print("Success")

else:
    print("Failed!")
