list = [1,2,3]

# print(dir(list))

engine = iter(list)
# print(dir(engine))

try:
    print(next(engine))
    print(next(engine))
    print(next(engine))
    print(next(engine))
except StopIteration:
    print(dir(StopIteration))
# set = {1,2,3,4,5}
# print(dir(set))

# tuple = (1,2,3,4,5)
# print(dir(tuple))

# dicti = {1:1, 2:2}
# print(dir(dicti))

# print(dir(tuple))
