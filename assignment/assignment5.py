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

