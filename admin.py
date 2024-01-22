from account import Account
from exp import WrongOperation
import datetime
class Admin():
    def addAccount(self):
        accno=int(input("ENTER ACCOUNT NO          :"))
        accname=input("ENTER ACCOUNT HOLDER NAME   :")
        acctype=input("ENTER ACCOUNT TYPE          :")
        balance=int(input("ENTER ACCOUNT BALANCE  :"))
        a1=Account(accno,accname,acctype,balance)
        with open("accountdetails.txt","a") as fp:
              fp.write(str(a1))
              fp.write("\n")
        print("ACCOUNT ADDED SUCCESFULLY ✅")

    def delAccount(self,accno):
        container=[]
        flag=False
        with open("accountdetails.txt","r") as fp:
            for e in fp:
                list2=e.split(",")
                if(list2[0]==str(accno)):
                    flag=True
                    print("ACCOUNT DELETED SUCCESFULLY 🔚")
                    
                else:
                    container.append(e)
                    
            if(flag==True):
                with open("accountdetails.txt","w") as fp:
                    for x in container:
                        fp.write(x)
   
    def searchAccount(self,accno):
          with open("accountdetails.txt","r") as fp:
                for e in fp:
                    try:
                        e.index(str(accno),0,4)
                        print("-----------------------------------------------")
                        print("ACCOUNT FOUND 🔍🔍")
                        list2=e.split(",")
                        print("----------- ACCOUNT DETAIL---------------------")
                        print("ACCOUNT  NO        IS  :",list2[0])
                        print("ACCOUNT  NAME      IS  :",list2[1])
                        print("ACCOUNT  TYPE      IS  :",list2[2])
                        print("ACCOUNT  BALANCE   IS  :",list2[3])
                        print("-----------------------------------------------")
                        break
                    except ValueError:
                        pass
                else:
                    print("ACCOUNT NOT FOUND")
                    print("--------------------------")

    def transact(self,date11):
        fou=False
        with open("transaction.txt","r") as fp:
           for e in fp:
               try:
                        e.index(str(date11),30,50)
                        fou=True
                        print("-----------------------------------------------")
                        print(" TRANSACTIONS FOUND 🔍🔍")
                        list21=e.split(",")
                        print("ACCOUNT  NO        IS  :",list21[0])
                        print("ACCOUNT  NAME      IS  :",list21[1])
                        print("ACCOUNT  TYPE      IS  :",list21[2])
                        print("ACCOUNT  BALANCE   IS  :",list21[3])
                        print("TRANSACTION TYPE   IS  :",list21[4])
                        print("TRANSACTION DATE   IS  :",list21[5])
                        print("-----------------------------------------------")
                        

               
               except ValueError as expe:
                     pass
                    # print(expe)
                    # break


           if(fou==False):
                print(" NO  TRANSACTION FOUND")
                print("--------------------------")