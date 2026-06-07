## The Iterable : a playlist of song

# playlist = ["song A","song B", "song C"]
# # print(dir(playlist))

# #Build the iterator: the engine
# engine = iter(playlist) # or playlist.__iter__()

# print(dir(engine))

# # ## Pull item out manually
# print(next(engine)) #songA
# print(next(engine)) #sing B
# print(next(engine)) #song c
# # print(next(engine)) #this will raise stop iteration

##<< FOR LOOP >>#

# for song in playlist:
#     print(song)

# fruit = ["Apple","Cherry","Mango"]
# for fruits in fruit:
#     print(fruits)


# name = "Prince"
# print(dir(name))


#<<< WHILE LOOP >>#
# secret_number = 55
# guess_count = 5

# print(" Guess a number between 1 and 100")

# while guess_count > 0:
#     # Get a new guess EACH time through the loop
#     number = int(input("Enter your guess: "))
    
#     if number == secret_number:
#         print(" Congratulations! You guessed the correct number.")
#         break
#     elif number < secret_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
    
#     # Reduce remaining guesses by 1
#     guess_count -= 1
    
#     # Show remaining attempts
#     if guess_count > 0:
#         print(f"You have {guess_count} guess(es) left.\n")
#     else:
#         print(f" Game over! The secret number was {secret_number}.")


# grade = [70, 80, 86, 90, 85]
# engine = iter(grade)
# print(next(engine))
# print(next(engine))
# print(next(engine))


# names = ["Alice", "Bob", "Charlie", "Diana"]

# for name in names:
#     print(f"Hello, {name}!")

# count = 0
# for name in names:
#     if len(name) > 5:
#         count += 1

# print(count)


# print("Even numbers from 0 to 20:")
# for num in range(0, 21, 2):
#     print(num)
    

# print("Number printed from 10 to 1: ")
# for num in range(10,0,-1):
#     print(num)


# print("Multiplication table of 7:")
# for i in range(1, 11):
#     print(f"{i} × 7 = {i * 7}")

# scores =[78, 92, 55, 88, 64, 91, 73]
# total = 0
# for score in scores:
#     total += score
#     average = total / len(scores)

# print(f"total: {total}")
# print(f"Average: {average:.2f}")

# passing_count = 0
# for score in scores:
#     if score >= 60:
#         passing_count += 1
# print(f"Passing scores: {passing_count}")

# highest = scores[0]  # Start with the first score
# for score in scores:
#     if score > highest:
#         highest = score

# print(f"Highest score: {highest}")

# items = ["apple", "banana", "cherry", "date"]

# # Create an iterator object from the list
# item_iterator = iter(items)

# while True:
#     try:
#         item = next(item_iterator)
#         print(item.upper())
#     except StopIteration:
#         break


# password = ""
# attempts = 0

# while password != "python123":
#     password = input("Enter the password: ")
#     attempts += 1

# print("Welcome!")
# print("Attempts made:", attempts)


# Countdown using while loop
i = 10

while i > 0:
    print(i)
    i -= 1

print("Blast off!")

# Count up from 1 to 10 and print only odd numbers
num = 1

while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1
