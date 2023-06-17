import os
print(os.environ)
string=os.environ
with open("envvar.txt",'w')as w:
    w.writelines(r'string')