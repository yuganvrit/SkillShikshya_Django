# 5. Password Strength Checker
# Write check_password(password) that returns a score (Weak / Medium / Strong) based on:
# Length ≥ 8
# Contains uppercase and lowercase
# Contains digits
# Contains special characters (!@#$%^&*) Loop through the string manually (don't just use .isupper() shortcuts for everything) to practice character iteration.
# Concepts: String indexing, for loop, boolean flags, nested conditions.

def check_password(password):
    # print(len(password))

    if len(password) > 0:

        contains_digit = False
        contains_spec_char = False
        has_upper = False
        length_great_eig = False
        
        
        for char in password:
            print(char)
            
            if char == char.upper():
                has_upper = True
                # print(has_upper)

            if len(password)>=8:
                length_great_eig = True
                # print(length_great_eig)

            if char.isdigit():
                contains_digit = True
                # print(contains_digit)

            if char in '!@#$%^&*':
                contains_spec_char = True
                # print(contains_spec_char)
        
        # if(has_upper and contains_spec_char and contains_digit and length_great_eig):
        #     print("Strong Password")

        count = has_upper + contains_digit + contains_spec_char + length_great_eig
        # print(count)
        if count == 4:
            print('Strong password')
        elif count >1:
            print('Medium Password')
        else:
            print('Weak password')
    else:
        print("Please Enter valid password.....")



password = input("Enter the password: ")
check_password(password)