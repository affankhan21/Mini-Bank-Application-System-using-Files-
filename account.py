class Account:
    def __init__(self,accno,accname,acctype,balance):
        self.accno=accno
        self.accname=accname
        self.acctype=acctype
        self.balance=balance

    def __str__(self):
        return str(self.accno)+","+(self.accname)+","+(self.acctype)+","+str(self.balance)
    def display(self):
        print(self.accno)
        print(self.accname)
        print(self.acctype)
        print(self.balance)


#a1=Account(101,"affan","savings",5000)
#a1.display()
