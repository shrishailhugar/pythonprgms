dicta = {1: "a", 2: "b"}
for k, v in dicta.items():
    print(k, v)
    
lst1 = ['a', 1, 'b', 2]
dict1 = {lst1[i]: lst1[i + 1] for i in range(0, len(lst1), 2)}
print(dict1)
list1=[]
for k, v in dict1.items():
    list1.append(k)
    list1.append(v)
print(list1)


