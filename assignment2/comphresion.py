

list = [1,2,3]

try:
    height = list[10]
    print(height)
except IndexError as e:
    print(e)

else:
    print('error is not found')

finally:
    print('other error')
