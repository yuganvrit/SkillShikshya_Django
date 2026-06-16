"""
Password Strength Checker
---------------------------
check_password(password) loops through each character manually
(using ord() comparisons instead of relying purely on .isupper()/.islower()/etc.)
to detect uppercase, lowercase, digits, and special characters,
then returns a strength rating: "Weak", "Medium", or "Strong".
"""

SPECIAL_CHARACTERS = "!@#$%^&*"


def check_password(password):
    """Return 'Weak', 'Medium', or 'Strong' based on password complexity."""

    # Boolean flags for each requirement
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Manually loop through each character
    for char in password:
        char_code = ord(char)  # numeric code for the character

        # Uppercase letters: A-Z -> 65-90
        if 65 <= char_code <= 90:
            has_upper = True

        # Lowercase letters: a-z -> 97-122
        elif 97 <= char_code <= 122:
            has_lower = True

        # Digits: 0-9 -> 48-57
        elif 48 <= char_code <= 57:
            has_digit = True

        # Special characters from our allowed set
        elif char in SPECIAL_CHARACTERS:
            has_special = True

    has_min_length = len(password) >= 8

    # Count how many of the 5 criteria are satisfied
    criteria_met = sum([has_min_length, has_upper, has_lower, has_digit, has_special])

    # Decide the strength based on how many criteria passed
    if criteria_met == 5:
        return "Strong"
    elif criteria_met >= 3:
        return "Medium"
    else:
        return "Weak"


def explain_password(password):
    """Print a detailed breakdown of which criteria the password meets."""
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        char_code = ord(char)
        if 65 <= char_code <= 90:
            has_upper = True
        elif 97 <= char_code <= 122:
            has_lower = True
        elif 48 <= char_code <= 57:
            has_digit = True
        elif char in SPECIAL_CHARACTERS:
            has_special = True

    has_min_length = len(password) >= 8

    print(f"\nChecking password: {password}")
    print(f"  Length >= 8        : {'Yes' if has_min_length else 'No'}")
    print(f"  Has uppercase      : {'Yes' if has_upper else 'No'}")
    print(f"  Has lowercase      : {'Yes' if has_lower else 'No'}")
    print(f"  Has digit          : {'Yes' if has_digit else 'No'}")
    print(f"  Has special char   : {'Yes' if has_special else 'No'}")
    print(f"  Overall strength   : {check_password(password)}\n")


def main():
    print("=== Password Strength Checker ===")
    print(f"(Special characters considered: {SPECIAL_CHARACTERS})\n")

    while True:
        password = input("Enter a password to check (or press Enter to quit): ")
        if password == "":
            print("Goodbye!")
            break
        explain_password(password)


if __name__ == "__main__":
    main()