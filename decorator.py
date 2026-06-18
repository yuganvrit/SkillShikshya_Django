# def role_selector(func):

#     def wrapper(role):
#         if role in ['admin','editor','user']:
#             return func(role)
#         print('access denied')
        
#     return wrapper

# @role_selector
# def check_role(role):
#     print('Access Granted as', role)

# check_role('hero')
# check_role('user')

##classwork
## create a user of school management system 
# create multiple function with dedicated task like giving assignments, checkng bills, validating id cards 
#decorate each function with a permission_checker decorator so that only authorized user can call the function
# Permission Decorator


def permission_checker(func):
    def wrapper(user, *args):
        if user["role"] in ["admin", "teacher"]:
            return func(user, *args)
        else:
            print(f"Access Denied")
    return wrapper


# Function to give assignments
@permission_checker
def give_assignment(user, assignment, student_name):
    print(f"{user['name']} gave '{assignment}' to {student_name}")


# Function to check bills
@permission_checker
def check_bills(user, student_name):
    print(f"{user['name']} checked bills of {student_name}")


# Function to validate ID cards
@permission_checker
def validate_id_card(user, student_name):
    print(f"{user['name']} validated ID card of {student_name}")


# Users
admin = {
    "name": "Hari",
    "role": "admin"
}

teacher = {
    "name": "Sita",
    "role": "teacher"
}

student = {
    "name": "Prince",
    "role": "student"
}


# Function Calls
give_assignment(teacher, "Data Communication Homework", "Prince")
check_bills(admin, "Ram")
validate_id_card(teacher, "Shyam")


# Unauthorized User
give_assignment(student, "Math Homework", "Aman")
check_bills(student, "Ram")
validate_id_card(student, "Shyam")