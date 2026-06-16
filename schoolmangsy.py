#create a user of school managements system
 
#create multiple functions with dedicated tasks like giving asssistant,checking_biils
# ,validting_id_card
 
#decorate each function a permisson_checker decorator so that only authroized 
# user can call the function

# Permission Checker Decorator

def permission_checker(required_role):
    def decorator(func):
        def wrapper(user):
            if user.get("role") == required_role:
                return func(user)
            else:
                print(f"❌ Access Denied! {user['name']} is not authorized to perform this action.")
        return wrapper
    return decorator


# Function: Give Assignment Access
@permission_checker("admin")
def give_assignment(user):
    print(f"✅ Assignment assigned successfully by {user['name']}.")


# Function: Check Bills
@permission_checker("accountant")
def check_bills(user):
    print(f"✅ Bills checked by {user['name']}.")


# Function: Validate ID Card
@permission_checker("security")
def validate_id_card(user):
    print(f"✅ ID Card validated by {user['name']}.")


# Users
admin_user = {
    "name": "Samir",
    "role": "admin"
}

accountant_user = {
    "name": "Ram",
    "role": "accountant"
}

security_user = {
    "name": "Hari",
    "role": "security"
}

student_user = {
    "name": "Sita",
    "role": "student"
}


# Function Calls
give_assignment(admin_user)      # Allowed
check_bills(accountant_user)    # Allowed
validate_id_card(security_user) # Allowed

print("-" * 40)

# Unauthorized Access Attempts
give_assignment(student_user)
check_bills(student_user)
validate_id_card(student_user)