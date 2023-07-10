tuple1=(1,2)
tuple2=tuple(tuple1)
print(tuple1 is tuple2)
print(id(tuple1)," ",id(tuple2))

list1=[1,2]
list2=list(list1)
list3=list1
print(list1 is list2)
print(id(list1)," ",id(list2)," ",id(list3))

