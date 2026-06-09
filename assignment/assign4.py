#. Reverse WORDS in a sentence: 'hello world' → 'world hello'

sentence = 'hello world this is Santosh' # input("Enter any sentence: ")

# a, b = sentence.split(" ")
# reverseString = f'{b} {a}'
# print(reverseString)

revStr = ""
lst = sentence.split(" ")
length = len(lst)
print(lst)
for i in range(length-1, -1, -1) :
    print(lst[i], end=" ")
    

print(revStr)