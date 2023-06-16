class Book():
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return(f"Book name is {self.name} and price is {self.price}")

    def __len__(self):
        return(200)

b=Book("shreeGUru","Infinity")

print(b)
print(len(b))