# Current logged-in user
# current_user = {
#     "name": "Samir",
#     "role": "editor"
# }

# # Decorator factory
# def require_role(required_role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if current_user["role"] == required_role:
#                 return func(*args, **kwargs)
#             else:
#                 print("Access Denied")
#         return wrapper
#     return decorator


# @require_role("admin")
# def delete_user():
#     print("User deleted successfully")


# @require_role("editor")
# def edit_article():
#     print("Article edited successfully")


# delete_user()
# edit_article()

#Create a function analyze_text(text) that returns a dictionary with:
#Total word count Total character count (excluding spaces)
#Most frequent word Number of sentences (split by ., !, ?) 
#Concepts: String methods, for loop, dictionary counting, split(), conditions.

# def analyze_text(text):
#     # Count words
#     words = text.split()
#     word_count = len(words)

#     # Count characters excluding spaces
#     char_count = len(text.replace(" ", ""))

#     # Find most frequent word
#     frequency = {}

#     for word in words:
#         word = word.lower().strip(".,!?")
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1

#     most_frequent_word = ""
#     max_count = 0

#     for word, count in frequency.items():
#         if count > max_count:
#             max_count = count
#             most_frequent_word = word

#     # Count sentences
#     sentence_count = 0
#     for char in text:
#         if char in ".!?":
#             sentence_count += 1

#     return {
#         "Total word count": word_count,
#         "Total character count": char_count,
#         "Most frequent word": most_frequent_word,
#         "Number of sentences": sentence_count
#     }


# # Example
# text = "Python is great. Python is easy to learn! Do you like Python?"

# result = analyze_text(text)

# for key, value in result.items():
#     print(f"{key}: {value}")

# smart calculator with history

# def calculate(num1, num2, operator):
#     match operator:
#         case "+":
#             return num1 + num2
#         case "-":
#             return num1 - num2
#         case "*":
#             return num1 * num2
#         case "/":
#             if num2 == 0:
#                 return "Error: Division by zero!"
#             return num1 / num2
#         case "**":
#             return num1 ** num2
#         case "%":
#             if num2 == 0:
#                 return "Error: Division by zero!"
#             return num1 % num2
#         case _:
#             return "Invalid operator!"


# history = []

# while True:
#     print("\n===== SMART CALCULATOR =====")
#     print("1. Calculate")
#     print("2. View History")
#     print("3. Quit")

#     choice = input("Enter your choice (1-3): ")

#     match choice:
#         case "1":
#             try:
#                 num1 = float(input("Enter first number: "))
#                 operator = input("Enter operator (+, -, *, /, **, %): ")
#                 num2 = float(input("Enter second number: "))

#                 result = calculate(num1, num2, operator)

#                 print("Result:", result)

#                 # Save calculation to history
#                 calculation = (num1, operator, num2, result)
#                 history.append(calculation)

#                 # Keep only last 10 calculations
#                 if len(history) > 10:
#                     history.pop(0)

#             except ValueError:
#                 print("Please enter valid numbers!")

#         case "2":
#             if not history:
#                 print("No calculations yet.")
#             else:
#                 print("\n--- Calculation History ---")
#                 for num1, operator, num2, result in history:
#                     print(f"{num1} {operator} {num2} = {result}")

#         case "3":
#             print("Goodbye!")
#             break

#         case _:
#             print("Invalid choice! Please select 1, 2, or 3.")

# todo list manager

# tasks = []


# def add_task():
#     title = input("Enter task title: ")
#     priority = input("Enter priority (high/medium/low): ").lower()

#     task = {
#         "title": title,
#         "priority": priority,
#         "done": False
#     }

#     tasks.append(task)
#     print("Task added successfully!")


# def view_tasks():
#     if not tasks:
#         print("No tasks available.")
#         return

#     print("\n--- TASKS ---")
#     for index, task in enumerate(tasks, start=1):
#         status = "✓" if task["done"] else "✗"

#         print(
#             f"{index}. {task['title']} | "
#             f"Priority: {task['priority']} | "
#             f"Done: {status}"
#         )


# def mark_done():
#     view_tasks()

#     if not tasks:
#         return

#     try:
#         task_num = int(input("Enter task number to mark as done: "))

#         if 1 <= task_num <= len(tasks):
#             tasks[task_num - 1]["done"] = True
#             print("Task marked as completed!")
#         else:
#             print("Invalid task number.")

#     except ValueError:
#         print("Please enter a valid number.")


# def delete_task():
#     view_tasks()

#     if not tasks:
#         return

#     try:
#         task_num = int(input("Enter task number to delete: "))

#         if 1 <= task_num <= len(tasks):
#             removed_task = tasks.pop(task_num - 1)
#             print(f"Deleted: {removed_task['title']}")
#         else:
#             print("Invalid task number.")

#     except ValueError:
#         print("Please enter a valid number.")


# def filter_by_priority():
#     priority = input(
#         "Enter priority to filter (high/medium/low): "
#     ).lower()

#     found = False

#     print(f"\n--- {priority.upper()} PRIORITY TASKS ---")

#     for task in tasks:
#         if task["priority"] == priority:
#             status = "✓" if task["done"] else "✗"

#             print(
#                 f"{task['title']} | "
#                 f"Done: {status}"
#             )
#             found = True

#     if not found:
#         print("No matching tasks found.")


# while True:
#     print("\n===== TODO LIST MANAGER =====")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Mark Task Done")
#     print("4. Delete Task")
#     print("5. Filter By Priority")
#     print("6. Exit")

#     choice = input("Enter choice: ")

#     match choice:
#         case "1":
#             add_task()

#         case "2":
#             view_tasks()

#         case "3":
#             mark_done()

#         case "4":
#             delete_task()

#         case "5":
#             filter_by_priority()

#         case "6":
#             print("Goodbye!")
#             break

#         case _:
#             print("Invalid choice.")

#  Password Strength Checker

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special = False

#     special_chars = "!@#$%^&*"

#     for char in password:
#         # Check uppercase manually
#         if 'A' <= char <= 'Z':
#             has_upper = True

#         # Check lowercase manually
#         elif 'a' <= char <= 'z':
#             has_lower = True

#         # Check digit manually
#         elif '0' <= char <= '9':
#             has_digit = True

#         # Check special character
#         elif char in special_chars:
#             has_special = True

#     score = 0

#     if len(password) >= 8:
#         score += 1

#     if has_upper and has_lower:
#         score += 1

#     if has_digit:
#         score += 1

#     if has_special:
#         score += 1

#     if score <= 1:
#         return "Weak"
#     elif score <= 3:
#         return "Medium"
#     else:
#         return "Strong"


# # Test
# password = input("Enter password: ")
# print("Strength:", check_password(password))

# Rock_paper_scissors-tournament


# import random

# choices = ["rock", "paper", "scissors"]

# score = {
#     "player": 0,
#     "computer": 0,
#     "draws": 0
# }


# def determine_winner(player, computer):
#     if player == computer:
#         return "draw"

#     if (
#         (player == "rock" and computer == "scissors") or
#         (player == "scissors" and computer == "paper") or
#         (player == "paper" and computer == "rock")
#     ):
#         return "player"
#     else:
#         return "computer"


# rounds = 0

# while rounds < 5 and score["player"] < 3 and score["computer"] < 3:
#     print("\n--- ROUND", rounds + 1, "---")

#     player_choice = input("Choose rock, paper, or scissors: ").lower()

#     if player_choice not in choices:
#         print("Invalid choice! Try again.")
#         continue

#     computer_choice = random.choice(choices)

#     print("Computer chose:", computer_choice)

#     result = determine_winner(player_choice, computer_choice)

#     if result == "player":
#         score["player"] += 1
#         print("You win this round!")
#     elif result == "computer":
#         score["computer"] += 1
#         print("Computer wins this round!")
#     else:
#         score["draws"] += 1
#         print("It's a draw!")

#     rounds += 1

#     print("\nScoreboard:")
#     print("Player:", score["player"])
#     print("Computer:", score["computer"])
#     print("Draws:", score["draws"])


# print("\n===== FINAL RESULT =====")

# if score["player"] > score["computer"]:
#     print("🎉 You are the overall winner!")
# elif score["computer"] > score["player"]:
#     print("💻 Computer wins the tournament!")
# else:
#     print("🤝 The tournament is a draw!")

# fibonacci and prime hybrid

# def fibonacci(n):
#     fib = []

#     a, b = 0, 1

#     for _ in range(n):
#         fib.append(a)
#         a, b = b, a + b

#     return fib
# def is_prime(num):
#     if num <= 1:
#         return False

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False

#     return True

# def fib_primes(n):
#     fib_sequence = fibonacci(n)
#     primes = []

#     for num in fib_sequence:
#         if is_prime(num):
#             primes.append(num)

#     return primes
# n = int(input("Enter number of Fibonacci terms: "))

# print("Fibonacci Sequence:", fibonacci(n))
# print("Prime Fibonacci Numbers:", fib_primes(n))

# contact book


contacts = {
    "Samir": {
        "phone": "9800000000",
        "email": "samir@gmail.com",
        "city": "Kathmandu"
    }
}

contacts = {}


# 1. Add Contact
def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }

    print("Contact added successfully!")


# 2. List All Contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- ALL CONTACTS ---")
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"City: {info['city']}")


# 3. Search Contact (Case-insensitive + partial match)
def search_contact():
    query = input("Enter name to search: ").lower().strip()

    found = False

    for name, info in contacts.items():
        if query in name.lower():
            print("\n--- MATCH FOUND ---")
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"City: {info['city']}")
            found = True

    if not found:
        print("No matching contact found.")


# 4. Update Contact
def update_contact():
    name = input("Enter exact name to update: ").strip()

    if name in contacts:
        print("Leave blank if you don't want to change a field.")

        phone = input("New phone: ").strip()
        email = input("New email: ").strip()
        city = input("New city: ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if city:
            contacts[name]["city"] = city

        print("Contact updated successfully!")
    else:
        print("Contact not found.")


# 5. Delete Contact
def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


# MENU LOOP
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            add_contact()

        case "2":
            list_contacts()

        case "3":
            search_contact()

        case "4":
            update_contact()

        case "5":
            delete_contact()

        case "6":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice. Try again.")

# nested dictionary structure
# contacts[name] = {
#     "phone": phone,
#     "email": email,
#     "city": city,
# }

# #Case-Insensitive Partial Search
# if query in name.lower():

# # Loop Through Dictionary
# for name, info in contacts.items():

# # safe update logic
# if phone:
#     contacts[name]["phone"] = phone

#    