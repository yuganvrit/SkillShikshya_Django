#Indexing

listItems = ['Apple', 'Ball', 'Cat']
print(listItems[0])

listItems2 = [1, 2, 3, 7, 8, 6, 4, 5, 7, 5, 6, 5, 8, 5, 3, 4]
print(listItems2[len(listItems2)-1])

#Slicing

print(listItems2[3:5])

items = [1, 2, 3, 4, 5]
print(id(items))
print(items[::-2])

#Built in methods of List

items.append(6)
print(id(items))

#Insert Method to insert value at specific index
items.insert(1, 20)
print(items)

items[0] = 200
print(items)

#Remove method to remove list items
items.remove(5)
print(items)

#Pop method to remove last item

# emp_list = []
# emp_list.pop()
# print(emp_list)

items.pop()
print(items)

#Index method to print index of a value inside list
print(items.index(20))

#Count Method to count number of same items inside list
items.count(200)
print(items)

#Extend method to merge 2 list
items2 = [5, 6, 7]
items.extend(items2)
print(items)

#Sort method 
items.sort()
print(items[0])
print(items[-1])




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Task1: Print last 5 items from list
print(my_list[-5:])

#Task2: Print max and min value from list
print(min(my_list))
print(max(my_list))

my_list.sort()
print(my_list[0])
print(my_list[-1])

#Task3: Print middle item from an odd list
odd_list = [1, 2, 3, 4, 5]
mid_item = odd_list[(len(odd_list)-1)// 2]
print(mid_item)

arr = [20, 10, 5, 80, 40, 60, 100]
print(arr)
arr.sort()
print(arr)