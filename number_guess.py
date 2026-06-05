number = 15
count = 5
while count >0  :
    guess =int(input("Enter the number you guess: "))
    if(guess == number):
        print("Congratulations you win")
        break
    elif(guess > number):
        print("Too high! Try again")
    elif(guess < number):
        print("Too low!! Try again")

    else:
        print("only number is required to enter ")
    count -= 1

    if(count == 0):
        print("You lost!! the correct number is ",number)