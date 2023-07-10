import sys
import dis
list1=[1,2]
tuple1=(1,2)
set1={1,2}
dict1={1:2}
print(sys.getsizeof(list1)," ",sys.getsizeof(tuple1)," ",sys.getsizeof(set1)," ",sys.getsizeof(dict1))

