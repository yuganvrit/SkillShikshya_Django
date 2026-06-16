# school mgmt system
# create multiple functions with dedicated tasks like giving assignment, checking bills, validating_id_card
# decorate each function a permission_checker decorator so taht only authorized usr van call teh function

member = {}
check = {"y": True, "n": False}


def permission_checker(allowed_roles):
    def wrapper(func):
        def role_checker(*args):
            operator_role = input("Enter your role: ").strip().lower()
            if operator_role in allowed_roles:
                return func(*args)
            print("Access Denied!!!")

        return role_checker

    return wrapper


@permission_checker(["principal", "admin"])
def admission(name, has_id, assignment_provided, bill, role="student"):
    member[name] = {
        "has_id_card": has_id,
        "assignment_provided": assignment_provided,
        "role": role,
        "bill": bill,
    }
    print("Student added successfully...")


@permission_checker(["admin", "teacher"])
def validating_id_card(name):
    if member[name]["has_id_card"]:  # ✅ correct
        print("The student has a valid id card.")
    else:
        print("The student does not have a valid id card.")


@permission_checker(["admin"])
def checking_bills(name):
    print(f"Bill amount: {member[name]['bill']}")


@permission_checker(["admin", "teacher"])
def giving_assignment(name):
    if member[name]["assignment_provided"]:
        print("Assignment already submitted.")
    else:
        mark = input("Mark as completed? y/n: ")
        while mark not in ["y", "n"]:
            mark = input("Enter y or n only: ")
        if check[mark]:
            member[name]["assignment_provided"] = True
            print("Assignment marked as completed.")


@permission_checker(["admin", "teacher", "principal"])
def show_all_students():
    if not member:
        print("No students added yet.")
        return
    print(f"{'Name':>15} {'Id Card':>15} {'Assignment':>15} {'Role':>15} {'Bill':>15}")
    for name, data in member.items():
        print(
            f"{name:>15} {str(data['has_id_card']):>15} {str(data['assignment_provided']):>15} {data['role']:>15} {data['bill']:>15}"
        )


def check_student(name):
    if name in member:
        return True
    print("The student is not present.")


while True:
    # print(student)
    print("""
    1. Add Student
    2. Check Id Card
    3. Check Assignment
    4. Checking Bill
    5. Show all students
    6. Exit\n
    """)

    try:
        choice = int(input("Enter the choice you want to select: "))
    except Exception:
        print("Enter the valid choice....")
        continue
    if choice not in range(1, 7):
        print("Please select a valid Option....")
    else:
        match choice:
            case 1:
                name = input("Enter the name of student: ").strip().lower()
                if name == "":
                    print("Please Enter your name.")
                    continue
                has_id_card = (
                    input("Does the student has Id Card?: y/n ").strip().lower()
                )
                while has_id_card not in ["y", "n"]:
                    has_id_card = input("Please enter y or n: ")
                assignment_provided = (
                    input("Is any assignment Provided? y/n : ").strip().lower()
                )
                while assignment_provided not in ["y", "n"]:
                    assignment_provided = input("Please enter y or n: ")

                try:
                    bill = int(input("Enter the bill amt:"))
                except Exception:
                    print("Please enter only numbers..")
                    continue

                admission(name, check[has_id_card], check[assignment_provided], bill)
            case 2:
                name = (
                    input("Enter the name of the student to check id card: ")
                    .strip()
                    .lower()
                )
                if check_student(name):
                    validating_id_card(name)

            case 3:
                name = (
                    input("Enter the name of student to provide assignment: ")
                    .strip()
                    .lower()
                )
                if check_student(name):
                    giving_assignment(name)

            case 4:
                name = (
                    input("Enter the name of the student to check bill: ")
                    .strip()
                    .lower()
                )
                if check_student(name):
                    checking_bills(name)

            case 5:
                show_all_students()

            case 6:
                break
