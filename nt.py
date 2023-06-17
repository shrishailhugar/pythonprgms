a="I am abc"
b=[]
ind=[]
b=a.split(" ")
for i in a:
    if i==" ":
        ind.append(a.index(i))
x=''.join(b)
y=x[::-1]
for i in range(len(ind)):
    y=y.replace(y[ind[i]]," "+y[ind[i]])
print(y)
print(ind)