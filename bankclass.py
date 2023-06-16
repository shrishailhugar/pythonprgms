class Bankaccount():
    minbalance=500
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("After adding {} your balance is {}".format(amount,self.balance))
    def withdraw(self,amount):
        amountleaving=self.balance-amount
        if((amountleaving)<Bankaccount.minbalance):
            print("we can't proceed your transaction as it's shortening minbalance your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            print("after withdrawing {} you left with {}".format(amount,self.balance))

accname=input("Enter Accountant name: ")
balance=int(input("Enter initial Deposit: "))
acc=Bankaccount(accname,balance)
 
i=0
while(i==0):
    trans=int(input("Press 1 to Deposit 2 to withdraw"))
    if trans==1:
        
        acc.deposit(int(input("Enter amount to deposit")))

    else:
        acc.withdraw(int(input("Enter amount to be withdrawn")))
    
    i=int(input("Enter 0 to continue 1 to stop:"))