count = 0
while True:
    try:
        print("""
              1. Sum 
              2. Subtract
              3. Multiply
              4. Divide
              5. Exit   
            """)

        choice = int(input("Enter choice:  "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            result = num1 / num2
        elif choice == 5:
            break
        else:
            print("Enter valid option.")
            continue

        print(f"Result: {result}")

    except ValueError as e:
        print(e)
        print("Please enter valid numbers")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    finally:
        count +=1
        print(f"Calculator solved {count} problems.")
