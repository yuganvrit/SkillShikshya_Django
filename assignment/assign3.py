#4. Check if a number is PRIME using loops

num = int(input("Enter the number: "))
count = 0

for i in range(2,num):
    if num % i ==0:
        count+=1

if (count >= 1):
    print("This is not Prime number")
else:
    print("This is a Prime number")