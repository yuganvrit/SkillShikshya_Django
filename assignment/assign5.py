#. Count VOWELS, CONSONANTS & DIGITS in a string
str = input("Enter the string: ")

vowels = 0
consonants = 0
digits = 0

vowelslst = ['a', 'e','i','o','u']
if len(str) >0:
    for i in str:
        if i.isdigit():
            digit += 1
        elif i in vowelslst:
            vowels += 1
        elif i.isalpha() and ( i not in vowelslst):
            consonants += 1
        else:
            print(f"{i} is neither vowel nor digit or consolant.")

print(f'vowels: {vowels} \nconsonants: {consonants} \ndigits: {digits}')