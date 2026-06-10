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



# c/w 
#reverse the string using function

# def revstr(string):
#     revstring = ''
#     for i in string:
#         revstring = i +revstring
#     return revstring

# def revstr(string):
#     stri = ''
#     for i in range(len(string)-1, -1, -1):
#         stri += string[i]
#     return stri

def revstr(string):
    return string[::-1]

print(revstr('santosh'))

for i, val in enumerate(lst):
    print(f'{i}=>{val}')

names = ['a', 'b']
score = [1,2]


#zip loops over each iterable at once. from names it gets names[0], similarly from score it gets score[0]
for n,s in zip(names,score):
    print(n,s)


#sorted
dic = ['alan', 'bob','ram', 'harishak']
print(sorted(dic, key=len , reverse=True))