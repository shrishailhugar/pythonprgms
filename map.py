def findlen(a):
    yield len(a)


list1=['123','12','5677']
mapobj=map(findlen,list1)
# print(*mapobj)
print(type(mapobj))
# print(*mapobj)

# print(next(next(mapobj)))

for x in ((mapobj)):
    print(next(x))