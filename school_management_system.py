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

    def __repr__(self):
        return f"User(name={self.name}, role={self.role})"


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

            return func(user, *args, **kwargs)
        return wrapper
    return decorator


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
