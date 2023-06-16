class Circle():
    pi=3.14#class attribute
    def __init__(self,radius=1):#by default the value is 1 and self is to show that it's the method of instance class it's not a function
        self.r=radius
        self.area=self.r*self.r*Circle.pi#Here pi called with class 

    def circumference(self):
        return self.r*2*self.pi#Here pi called with instance

c1=Circle(3)
print(c1.area)
print(c1.circumference())