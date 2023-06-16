# it's type is range not list
list1=range(5)
type(list1)

list2=range(6,10)
zipa=zip(list1,list2)
print(zipa,"   ",*zipa)
print(list1[0])
list3=[(x+y) for (x,y) in zip(list1,list2)]
list4=[(x,y) for x in list1 for y in list2 ]
print(list3)

for a in (list1,list2):
    print(a)