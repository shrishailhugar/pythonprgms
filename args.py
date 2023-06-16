def addallpassednumers(a,*args):
    sum = 0
    sum+=a
    for arg in args:
        sum += arg
    
    return (sum)
    
print(addallpassednumers(100,1,2,3,45,6,7,8,6))