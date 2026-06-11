history = []

while True:
    if len(history) >= 10:
        del history[0]

    operation = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/',
        '5': '**',
        '6': '%',
    }

    print('-' *45)
    process = input(
        "\n\nEnter the operation you want to perform\n1.sum \n2.Subtraction \n3.multiply \n4.division \n5.power \n6.reminder \n7.Read History\n\n"
    )


    if process != '7':
        firstNo = int(input("Enter the first number: "))
        SecondNo = int(input("Enter the second number: "))

        history.append((firstNo, SecondNo, operation[process]))

    match process:
        case "1":
            print("Sum: ", firstNo + SecondNo)
            print('-' *45)

        case "2":
            print("Subtraction: ", firstNo - SecondNo)
            print('-' *45)

        case "3":
            print("Multiplication: ", firstNo * SecondNo)
            print('-' *45)

        case "4":
            if SecondNo != 0:
                print("Division: ", firstNo / SecondNo)
            print("Second number should not be zero.")
            print('-' *45)

        case "5":
            print("Power: ", firstNo**SecondNo)
            print('-' *45)

        case "6":
            print("Remainder: ", firstNo % SecondNo)
            print('-' *45)
        
        case '7':
            for i in history:
                print(f'First Number: {i[0]} Second Number: {i[1]} Operation: {i[2]}')
            print('-' *45)
        case _:
            print("Invalid input. Please try again.")