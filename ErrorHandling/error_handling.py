# error handling

# try except block 
dictionary = {
    'name': 'Sahil',
    'height': "5ft 10"
}

try:
    weight = dictionary['weight']

except: 
    print("something went wrong")


# another example
list = [1,2,3,4,5]
try:
    weight = list[10]

except IndexError as e: 
    print(e)

finally:
    print('other error')



list2 = [1,2,3,4,5]
try:
    weight = list2[1]

except IndexError as e: 
    print(e)

else:
    print("error not found")

finally:
    print('other error')



# task
# 0div, string input
