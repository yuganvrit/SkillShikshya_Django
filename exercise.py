# grades = [1,2,3,4,5]

# engine = iter(grades)

# print(next(engine))
# print(next(engine))
# print(next(engine))
# print(next(engine))
# print(next(engine))


# #2:
# names = ['Alice', 'bob', 'charlie', 'diana']
# for name in names:
#     print(f"Hello, {name}!")

# count = 0
# for name in names:
#     if(len(name) > 5):
#         count+=1

# print(f"{count} names have more than 5 words.")

# even = 0
# odd = 0

# num1 = int(input("Enther the first number: "))
# num2 = int(input("Enther the second number: "))

# for i in range(num1, num2+1):
#     if (i%2 ==0):
#         even += i
#     else:
#         odd += i

# print(even, odd)

#3.

# for i in range(0, 21):
#     print(i)
    
# for i in range(10, 0, -1):
#     print(i)


# # 4.

# scores = [78,92,55,88,64,91,73]

# total =0
# for i in scores:
#     total += i

# avg = total/len(scores)

# count = 0
# for i in scores:
#     if(i >= 60):
#         count += 1

# print(f"{count } scores are passing by more or equal to 60 ")

# max = 0
# for i in scores:
#     if max < i:
#         max = i

# print(f'the maximum number is: {max}')


# #5.
# num = 10
# while num > 0:
#     print(num)
#     num-=1

# #6.

# pwd = 'python123'
# counter = 0
# while True:
#     password = input("Enter the password: ")
#     if password == pwd:
#         print("Welcome! you made {counter} attempts")
#         break
#     counter +=1

# #7.
# items = ['apple', 'banana','chhery','date']

# while True:
#     try:
#         engine = iter(items)
#         print(next(engine).upper())
#         print(next(engine).upper())
#         print(next(engine).upper())
#         print(next(engine).upper())
#         print(next(engine).upper())
#         print(next(engine).upper())

#     except StopIteration:
#         break


