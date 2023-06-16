def addmarksofstudents(**k):
    sum = 0
    print(k['h'])
    for k, v in k.items():
        sum += v
    return (sum)

print(addmarksofstudents(k=95,E=90,h=85))


def addmarkswithcota(a,*args, **kwargs):
    sum = 0
    print(args[0])
    sum = args[0] + args[1]+a
    for k, v in kwargs.items():
        sum += v
        
    return sum

aarg = (10, 20)
karg = {'k': 95, 'E': 90, 'h': 85}

print(addmarkswithcota(5,*aarg,**karg))