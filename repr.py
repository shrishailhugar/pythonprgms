#converting regular stting to raw string
#path =C:\Users\ninga\teamwork
#for above path if we directly pass then python treats \n as newline and \t as tab
#to avoid that use repr func 

# path='C:\Users\ninga\teamwork'
# the above line throw an unicodeescape error 

path=r'C:\Users\ninga\teamwork'

passingpath=repr(path)
# the repr function going to add extra \ to escape 

print(path)
print(passingpath)