#check if two strings are anagrams(e.g. "listen" and "silent")

def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):  # fast reject
        return False
    
    return sorted(str1) == sorted(str2)  # full check
print(anagrams("listen", "silent"))