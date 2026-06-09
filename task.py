## 1
# number = [1,2,9,5,6]
# largest = number[0]
# second_largest = number[1]
# for num in number:
#     if num > largest:
#         largest = num

#     elif second_largest < largest and num != largest:
#         second_largest = num

# print(f"largest: {largest}")
# print(f"second_largest: {num}")


## 2
# str1 = "listen"
# str2 = "silent"

# if len(str1) != len(str2):
#     print("Not Anagram")
# else:
#     count = 0

#     for char in str1:
#         if char in str2:
#             count += 1

#     if count == len(str1):
#         print("Anagram")
#     else:
#         print("Not Anagram")

## 4

number = 17

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("It is a Prime Number")
else:
    print(" It is not a Prime Number")
