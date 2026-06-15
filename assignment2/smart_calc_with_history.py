history = []

operation = {
    1: "+",
    2: "-",
    3: "*",
    4: "/",
    5: "**",
    6: "%",
}


def calculation(firstNo, SecondNo, process):
    match process:
        case 1:
            print(firstNo + SecondNo)
            print("-" * 45)

        case 2:
            print("Subtraction: ", firstNo - SecondNo)
            print("-" * 45)

        case 3:
            print("Multiplication: ", firstNo * SecondNo)
            print("-" * 45)

        case 4:
            if SecondNo == 0:
                print("Second number should not be zero.")
            else:
                print("Division: ", firstNo / SecondNo)
            print("-" * 45)

        case 5:
            print("Power: ", firstNo**SecondNo)
            print("-" * 45)

        case 6:
            print("Remainder: ", firstNo % SecondNo)
            print("-" * 45)

        case 7:
            print("Exiting the program.")
        case _:
            print("Invalid input. Please try again.")


while True:
    if len(history) >= 10:
        del history[0]
    print("-" * 45)

    try:
        process = int(
            input(
                "\n\nEnter the operation you want to perform\n1.sum \n2.Subtraction \n3.multiply \n4.division \n5.power \n6.reminder \n7.Read History \n8.Exit\n\n"
            )
        )
        if process == 8:
            print("Exiting program.....")
            break

    except ValueError as e:
        print("Please select one option from the given list. Try again!! ")
        continue

    if process not in [1, 2, 3, 4, 5, 6, 7, 8]:
        print("The option you entered is invalid try again. ")
    elif process == 7:
        if not history:
            print("No history found!!")
        else:
            for i in history:
                print(f"First Number: {i[0]} Second Number: {i[1]} Operation: {i[2]}")
                print("-" * 45)
    else:
        try:
            firstNo = int(input("Enter the first number: "))
            SecondNo = int(input("Enter the second number: "))
            history.append((firstNo, SecondNo, operation[process]))
            calculation(firstNo, SecondNo, process)
        except ValueError:
            print("Choose one from the option!!")
