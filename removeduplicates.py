list1=[1,2,3,3,4,5,6,6,6,7,7,7]
set1=set(list1)
# dict1={j:dict1[j]+1 for i,j in enumerate(set1) for k in list1}
# print(dict1)
# x=[]
# [x.append(i) for i in list1 if i not in x]
# print(x)

dict1={j:0 for j in set1}

print(dict1)
print(dict1[1])

for i in list1:
    dict1[i]+=1

print(max(dict1.values()))
print(type(dict1))
maxvalues={m:value for m,value in dict1.items() if value==max(dict1.values()) }


print(maxvalues)
