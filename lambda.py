def myfun(n):
    return lambda a:a*n

mynum=myfun(3)
print(mynum)
print(mynum(2))

x=lambda a: a*3
print(x(3))