stringa="let me change"
ind=[]
for i in range(len(stringa)):
    if stringa[i]==" ":
        ind.append(int(i))

x=stringa.split(" ")
y=""
for a in x:
    y+=a

print(y)
y=(y[::-1])
y=list(y)
print(ind)
j=0
# iamabc
for i in range(len(y)+len(ind)):
    if i==ind[j]:
        m=y[i-j]           
        y[i-j]="  "+m
        j+=1
        if j==len(ind):
            break

for z in y:
    print(z,end="")






list1=[abs(12-x) for x in range(5)]
list2=[abs(12-x) for x in range(5,11)]
mergedlist=[list2,list1]
print("\n",mergedlist,"\n",mergedlist[0],"\n",mergedlist[1])

mergedlist.sort(reverse=True)
print(mergedlist)

print(mergedlist.__getitem__(1))
print(mergedlist.__len__())
print(stringa.__len__())
print(stringa.capitalize())
print(stringa.expandtabs())
print(stringa.find("t"))
print(stringa.find(" "))