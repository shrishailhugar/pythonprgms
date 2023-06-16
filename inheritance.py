class Animal():
    species="mammals"
    def __init__(self,name):
        self.nameofanimal=name
    def eat(self):
        print("I'm a animal and i'm eating")
class Dog(Animal):
    def __init__(self,breed,sound):
        Animal.__init__(self,"dog")
        self.breedofdog=breed
        self.sound=sound
    def speak(self):
        print("im a {} and my breed is {} and sounds like {} ".format(self.nameofanimal,self.breedofdog,self.sound))
    def eat(self):
         print("I'm a dog and i'm eating")
class Cat(Animal):
    def __init__(self,breed,sound):
        self.breedofcat=breed
        self.sound=sound
        Animal.__init__(self,"cat")
    def speak(self):
        print("im a {} and my breed is {} and sound like {} ".format(self.nameofanimal,self.breedofcat,self.sound))
dog1=Dog("pitbull","WOOF")
cat1=Cat("cutty","Meow")

print(dog1.speak())
print(cat1.speak())
print(dog1.eat)