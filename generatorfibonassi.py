def fibonassi(limit):

    *args,count=0,1,0
    # print(args[0],args[1])

    while(count<limit):
        args[0],args[1]=args[1],args[0]+args[1]
        yield args[0]
        count+=1

for i in fibonassi(10):
    # print(type(i))
    print(i)

    
# x=fibonassi(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))