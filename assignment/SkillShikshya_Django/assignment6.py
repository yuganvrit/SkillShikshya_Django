# reverse words in a sentence "hello worls" -> "world hello"

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

# Test
sentence = "hello world"
print(reverse_words(sentence))  