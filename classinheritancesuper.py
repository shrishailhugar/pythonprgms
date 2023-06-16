#if all the Base classes accepting same args then it will call constructor of first base class from left 
#class child(Base1,Base2) here it will call constructor of Base1 if we call with "super" keyword
#else if all Base class not accepting same args it will throw an error if we use "super"  to call Base class
class Base:
    def __init__(self,ngames=1,**k):
        print("BASE CLASS CONSTRUCTOR")
        self.pname=k['pname']
        self.age=k['age']
        self.ngames=ngames
        self._protvar=4
    
    def getplayerinfo(self):
        print(f"Player {self.pname} played {self.ngames} games in the age of {self.age} ",end=",")

class Base1:
    def __init__(self,ngames=1,**k):
        print("BASE1 CLASS CONSTRUCTOR")
        self.pname=k['pname']
        self.age=k['age']
        self.ngames=ngames

    
    def getplayerinfo(self):
        print(f"Player {self.pname} played {self.ngames} games in the age of {self.age} ",end=",")
class Base3:
    def __init__(self) -> None:
        print("Base3 constructor")

class kabaddi(Base,Base1):

    def __init__(self,fgame,**k):
        print('IN CHILD CLASS')
        self.fgame=fgame
        # Base.__init__(self,**k)
        super().__init__(**k)
        
        

    def getcompleteinfo(self):
        self.getplayerinfo()
        print(f"His fav game is {self.fgame}")


obj1=kabaddi("kabaddi",pname="Bapu",age=15,ngames=2)
obj1.getcompleteinfo()



