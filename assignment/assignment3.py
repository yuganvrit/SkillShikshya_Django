# find all duplicates in alist without using set()

def find_duplicates(arr):
    seen = []
    duplicates = []
    
    for item in arr:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)
    
    return duplicates

#  Test
list1 = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
print(find_duplicates(list1))  