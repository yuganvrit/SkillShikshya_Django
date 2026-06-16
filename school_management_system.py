<<<<<<< HEAD
# create a user of school management system 
# create multiple functions with dedicated tasks giving assignment, checking_bills, validiting_id_card
# decorate each functions a permission_checker decorator so that only authorized user can call the 
# function . # complete task.

# from functools import wraps
# school_user = {
#     'ram': 'editor',
#     'shyam': 'teacher',
#     'hari': 'accountant',
#     'sita': 'student',
# }

# def school_management_system(allowed_roles):
#     """Decorator factory: only allows users with a role in `allowed_roles`."""
#     def decorator(func):
#         @wraps(func)
#         def wrapper(username, *args, **kwargs):
#             role = school_user.get(username)
#             if role in allowed_roles:
#                 return func(username, *args, **kwargs)
#             else:
#                 print(f"Access Denied: '{username}' ({role}) cannot perform '{func.__name__}'")
#         return wrapper
#     return decorator


# @school_management_system(['teacher'])
# def giving_assignment(username, student, subject):
#     print(f"{username} gave an assignment on {subject} to {student}")

# @school_management_system(["accountant", "admin"])
# def checking_bills(username, student):
#     print(f"{username} checked bills for {student}")  

# @school_management_system(["admin"])
# def validating_id_card(username, student):
#     print(f"{username} validated ID card for {student}")

# # --- Testing ---
# giving_assignment("ram", "Sita", "Math")     # allowed (teacher)
# giving_assignment("shyam", "Sita", "Math")   # denied (accountant)

# checking_bills("shyam", "Hari")              # allowed (accountant)
# checking_bills("sita", "Hari")               # denied (student)

# validating_id_card("hari", "Ram")            # allowed (admin)
# validating_id_card("ram", "Ram")             # denied (teacher)

# create a user of school management system
class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role  # e.g. 'admin', 'teacher', 'accountant', 'staff', 'student'
=======
"""
School Management System
-------------------------
- Users have roles (admin, teacher, accountant, student, etc.)
- A `permission_checker` decorator restricts each function to specific roles
- Functions: give_assignment, check_bills, validate_id_card
"""

from functools import wraps


# ---------------------------------------------------------
# User class
# ---------------------------------------------------------
class User:
    def __init__(self, user_id, name, role):
        """
        role can be: 'admin', 'teacher', 'accountant', 'student', 'staff'
        """
        self.user_id = user_id
        self.name = name
        self.role = role
>>>>>>> cea37714169c1c8d82522dd4bb90166180e59255

    def __repr__(self):
        return f"User(name={self.name}, role={self.role})"


<<<<<<< HEAD
# decorator: permission_checker
from functools import wraps

def permission_checker(*allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.role not in allowed_roles:
                print(f"[DENIED] {user.name} ({user.role}) cannot call '{func.__name__}'")
                return None
=======
# ---------------------------------------------------------
# Permission decorator
# ---------------------------------------------------------
def permission_checker(*allowed_roles):
    """
    Decorator factory that restricts access to a function
    based on the calling user's role.

    Usage:
        @permission_checker("admin", "teacher")
        def some_function(user, ...):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, User):
                raise TypeError("First argument must be a User instance")

            if user.role not in allowed_roles:
                print(
                    f"[ACCESS DENIED] {user.name} (role: {user.role}) "
                    f"is not authorized to perform '{func.__name__}'. "
                    f"Allowed roles: {', '.join(allowed_roles)}"
                )
                return None

>>>>>>> cea37714169c1c8d82522dd4bb90166180e59255
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


<<<<<<< HEAD
# create multiple functions with dedicated tasks: giving assignment, checking_bills, validating_id_card

@permission_checker("teacher", "admin")
def giving_assignment(user, student_name, assignment_title):
    print(f"{user.name} gave '{assignment_title}' to {student_name}")


@permission_checker("accountant", "admin")
def checking_bills(user, student_name, amount_due):
    print(f"{user.name} checked bills for {student_name}: ${amount_due} due")


@permission_checker("staff", "admin")
def validating_id_card(user, student_id):
    print(f"{user.name} validated ID card: {student_id}")


# --- example usage ---
admin = User(1, "Mr. Sharma", "admin")
teacher = User(2, "Mrs. Gupta", "teacher")
student = User(3, "Anish", "student")

giving_assignment(teacher, "Anish", "Math HW")     # allowed
checking_bills(student, "Anish", 1500)             # denied
validating_id_card(admin, "STU2026001")            # allowed


    
=======
# ---------------------------------------------------------
# Functions with dedicated tasks
# ---------------------------------------------------------
@permission_checker("teacher", "admin")
def give_assignment(user, student_name, assignment_title):
    print(
        f"[ASSIGNMENT] {user.name} ({user.role}) gave '{assignment_title}' "
        f"to {student_name}."
    )


@permission_checker("accountant", "admin")
def check_bills(user, student_name, amount_due):
    print(
        f"[BILL CHECK] {user.name} ({user.role}) checked bills for "
        f"{student_name}: Amount due = ${amount_due}"
    )


@permission_checker("staff", "admin")
def validate_id_card(user, student_id):
    print(
        f"[ID VALIDATION] {user.name} ({user.role}) validated ID card "
        f"for student ID: {student_id}"
    )


# ---------------------------------------------------------
# Demo / Test
# ---------------------------------------------------------
if __name__ == "__main__":
    admin = User(1, "Mr. Sharma", "admin")
    teacher = User(2, "Mrs. Gupta", "teacher")
    accountant = User(3, "Mr. Joshi", "accountant")
    staff = User(4, "Ms. Rai", "staff")
    student = User(5, "Anish", "student")

    print("\n--- Valid access ---")
    give_assignment(teacher, "Anish", "Math Homework Chapter 5")
    check_bills(accountant, "Anish", 1500)
    validate_id_card(staff, "STU2026001")

    print("\n--- Admin (super user) access ---")
    give_assignment(admin, "Ravi", "Science Project")
    check_bills(admin, "Ravi", 2000)
    validate_id_card(admin, "STU2026002")

    print("\n--- Unauthorized access attempts ---")
    give_assignment(student, "Anish", "Try assign to self")
    check_bills(teacher, "Anish", 1500)
    validate_id_card(accountant, "STU2026003")
>>>>>>> cea37714169c1c8d82522dd4bb90166180e59255
