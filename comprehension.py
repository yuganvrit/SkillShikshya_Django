words = ["apple", "banana", "cat", "elephant", "dog", "python"]

result = [word.upper() for word in words if len(word) > 5]

print(result)