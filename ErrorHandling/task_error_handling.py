def calculator():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    choice = input("Choose an operation type\n 1 for addition \n 2 for subtraction \n 3 for division \n 4 for modulus\n")

    try: 
        if choice == '1':
            add = first_num + second_num
            print(f"The addition of {first_num} and {second_num} is {add}")
        elif choice == '2':
            sub = first_num - second_num
            print(f"The subtraction of {first_num} and {second_num} is {sub}")
        elif choice == '3':
            mul = first_num * second_num
            print(f"The multiplication of {first_num} and {second_num} is {mul}")
        elif choice == '4':    
            div = first_num / second_num
            print(f"The division of {first_num} and {second_num} is {div}")
        else:
            print("Error: Please enter the right choice!")
            
    except ValueError:
        print("Error: Please enter valid numbers!")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

    except Exception as e:
        print("An unexpected error occurred:", e)


calculator()
continue_calc = input("Do you want to continue using calculator: (type y or n)")
if continue_calc == 'y' or continue_calc == 'yes':
    calculator()
 