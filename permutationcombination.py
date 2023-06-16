pos=2
x=[[i,j] for i in range(pos) for j in range(pos)]
print(x)
chances=6
a=([[i+1,j+1,k+1] for i in range(chances) for j in range(chances) for k in range(chances) if i+j+k+3<=5])
print(a)
print(len(a))