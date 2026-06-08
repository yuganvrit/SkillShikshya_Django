#3. Find ALL DUPLICATES in a list without using set()

lst = [1,2,2,3,4,5,5]
duplicate = []

for i in lst:
    if lst.count(i) > 1:
        if i in duplicate:
            continue
        else:
            duplicate.append(i)

print(duplicate)