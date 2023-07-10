set1={1,2,3}
set1.add(4)
print(set1)

#it will not allow to add elements to the frozenset  it will throw an error
fset=frozenset(set1)
try:
    fset.add(5)
except AttributeError as e:
    print(e)
   
print("Fset after trying to add 5 into it",fset)

fset2=frozenset([1,2,3,5])
fset3=frozenset({1,2,3,4,4})
fset4=frozenset({1:2,3:4,3:4})
#these all will be in the set format
#it will delete the duplicate ele of the fset3
#it will list unique keys  of dict of fset4
print(fset2," ",fset3," ",fset4)

try:
    fset2.add(10)
    fset3.add(10)
    fset4.add(10)
except Exception as e:
    print(e)
