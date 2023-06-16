
#####################____________EXEC________________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#evaluate fun will evaluate the input

str1="str(1+2+3)+'hello'"
result=eval(str1)
print(result)

inp=input("Enter Maths expression:")
#Eval returns 10 for input(5+5*5-20) 
#eval returns - hello    """for print('hello')""""
#              - None
#feval returns -hello for 'hello' 
#if we provide hello as input instead of 'hello'  it treat is a variable
#(str(5+5)+hello) returns =10hello
res=eval(inp)
print(res)

#####################____________EXEC________________%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

execsimple=input("Enter exp:")
#it's going to execute script 
#for 5+5  it returns= None
#for pirnt('Hello') returns = hello
result=exec(execsimple)
print(result)



inst="""
def add(a,b):
    a=20
    b=20
    return a+b
x=add(5,6)
print(x)
"""
res=exec(inst)
#it's going to print - 11
#                    - None
print(res)

