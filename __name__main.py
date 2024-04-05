from packagefor_name_ import callfun

# callfun()

# this will yield print statements from package_name.py bcz once we import any package it will run that fun here "callfun" 
#which is written inside the package_namefolder  bcz there we not only defined we called as well

#if we don't call also the callfun() above here we it will print once bcz it's called in that original defined file(package_name.py)


# so __________USE__            __name__=="__main__"
# the above line not mean the file name should be __main__ each file if we are running it's main fun only 
# it will call it from here only it will accept call from packagefor_name.py file bcz if we were runnning this file only this is __main__


print(__name__' in source running file')
callfun()

#if we write callfun() in packagefor_name.py like this
def callfun():
   print('__name__',' inside callfun')
callfun()
#for 1st scenario it will yield
#__name__.funfile  inside callfun ----- this is during import it will run fun
#__main__                     ---- first print statement in this file(line 16)
#__name__.funfile  inside callfun ---- this is when we call cllfun()(line 17)

#if we write callfun() in packagefor_name.py like this
def callfun():
   print('__name__',' inside callfun')
if __name__=='__main__'    
    callfun()
# for 2nd scenario the output yield was
# __main__                       --here during import it will not call bcz __name__!='__main__' as it's ran from this file(__name__main) (line 16)
# __name__.funfile 	 inside callfun   --this is when callfun called(line 17)
