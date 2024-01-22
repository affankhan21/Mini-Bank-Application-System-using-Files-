from user import User
if(__name__=="__main__"):
    obj11=User()
    choice=0
    while(choice !=5):
        print(" 🖥️  🖥️  🖥️   🖥️  🖥️  🖥️  🖥️  🖥️  🖥️   🖥️  🖥️  🖥️ ")
        print("\t\t1.DISPLAY ACCOUNT BALANCE")
        print("\t\t2.WITHDRAW AMOUNT")
        print("\t\t3.DEPOSIT AMOUNT")
        print("\t\t4.TRANSFER")
        print("\t\t5.EXIT")
        choice=int(input("ENTER YOUR CHOICE :"))
        if (choice==1):
            accno=int(input("ENTER ACCOUNT  NUMBER TO DISPLAY BALANCE :"))
            obj11.displayBalance(accno)      
        
        elif (choice==2): 
            accno=int(input("ENTER ACCOUNT  NUMBER :"))
            amt=int(input("ENTER AMOUNT TO WITHDRAW :"))
            obj11.withdrawAmount(accno,amt)      
        elif (choice==3): 
            accno=int(input("ENTER ACCOUNT  NUMBER :"))
            amt1=int(input("ENTER AMOUNT TO DEPOSIT :"))
            obj11.depAmt(accno,amt1)    
        elif (choice==4):
            accno1=int(input("ENTER ACCOUNT  NUMBER 1 TO  CREDIT:"))
            accno2=int(input("ENTER ACCOUNT  NUMBER 2 TO DEBIT:"))
            amt1=int(input("ENTER AMOUNT TO TRANSFER :"))
            obj11.Transfer(accno1,accno2,amt1)
            
        elif(choice==5):
            print("THANK YOU FOR USING OUR APPLICATION🚀")