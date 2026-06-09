#find the second largest number in the list without using max()twice.
    

# list = [5, 2, 6, 9, 3]
# largest = list[0]
# second_largest = list[0]

# for i in list:
#     if i > largest:
#         second_largest = largest  # Previous largest becomes second
#         largest = i                # Update largest
#     elif i > second_largest and i != largest:
#         second_largest = i

# print("Largest:", largest)
# print("Second largest:", second_largest)

list = [1,9,7,5,8]

largest = 0
second_largest = 0

for num in list:
    if num > largest:
        largest = num

for num in list:
    if num > second_largest and num!= largest:
        second_largest = num

print(f"largest num is {largest}")
print(f"second largest num is {second_largest}")

# check if two strings are anagrams(e.g. "listen" and "silent")

def anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

# Test
# print(anagrams("listen", "silent"))  # True
# print(anagrams("hello", "world"))    # False
# print(anagrams("Debit Card", "Bad Credit"))  # True

# find all DUPLICATES in a list without using set()
def find_duplicates(arr):
    seen = []
    duplicates = []
    
    for item in arr:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    
    return duplicates

# Test
list1 = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
print(find_duplicates(list1))  # [2, 3, 1]

# check if a number is prime using loops.

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(1))   # False

# count vowels,consonants and digits in a string

def count_characters(text):
    vowels = 0
    consonants = 0
    digits = 0
    
    # Define vowels (both lowercase and uppercase)
    vowel_set = "aeiouAEIOU"
    
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
    
    return vowels, consonants, digits

# Test
text = "Hello World 123"
v, c, d = count_characters(text)
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}")
# Output: Vowels: 3, Consonants: 7, Digits: 3

# reverse words in a sentence "hello worls" -> "world hello"

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

# Test
sentence = "hello world"
print(reverse_words(sentence))  # Output: world hello





