def fib(limit):
    a,b=0,1

    while(a<limit):
        yield a
        t=a
        a=b
        b+=t
        



n=100
for  i in fib(n):
    print(i)