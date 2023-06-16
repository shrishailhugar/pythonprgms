listall=[[x for x in range(4)],[x for x in range(4,8)],[x for x in range(8,12)]]
lista=[x for temp in listall for x in temp]
print(listall,"   ",lista)


listall=[[x for x in range(4)],[x for x in range(4,9)],[x for x in range(9,15)]]
listcomb=[x for t in listall for x in t]
print(listall, " " ,listcomb )