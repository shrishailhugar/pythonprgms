# In Python, all objects and data structures are stored in the private heap and are managed by Python Memory Manager internally
#in python in order to do memory allocation and delete 
#for each object there will be object reference count
#As mentioned before, there are layers of abstraction from the physical hardware to CPython. The operating system (OS) abstracts the physical memory and creates a virtual memory layer that applications (including Python) can access.

import sys
import ctypes
#getrefcount
#  "it will always give +1 count as it will create another ref to get the count"
ref=[1,2]
print(sys.getrefcount(ref))
ref2=ref
print("ref count of ref with getrefcount=",sys.getrefcount(ref))
print("ref count of ref2 with getrefcount=",sys.getrefcount(ref2))
xref="1"
print(sys.getrefcount(xref))

#c_long.from_address from ctypes module it will give correct number of addresses.

print("ref count of ref with c_long.from_address=",ctypes.c_long.from_address(id(ref)).value)

ref3=ref2
print(f"Ref count of ref={ctypes.c_long.from_address(id(ref)).value} ref2={ctypes.c_long.from_address(id(ref2)).value} ref3={ctypes.c_long.from_address(id(ref3)).value} after ref3 referring ref1")

# setting ref3 to None
ref3=None
print(f"Ref count of ref={ctypes.c_long.from_address(id(ref)).value} after ref3 set to None")
print(ctypes.c_long.from_address(id(ref)))
