from admin import Admin
from user import User
import getpass
import random
import stdiomask

if(__name__=="__main__"):
    obj1=Admin()
    choice=0
    obj11=User()
    
    while (choice!=3):
        print("WELCOME TO BANK APPLICATION 🏦🏦🏦🏦🏦🏦")
        print("\t\t1.ADMIN")
        print("\t\t2.USER")
        print("\t\t3.EXIT")
        choice=int(input("ENTER CHOICE :"))
        if (choice==1):
            username=input('enter username:')
            password=stdiomask.getpass("enter password:",mask='*')
            otp=random.randint(1000,9999)
            print("YOUR ADMIN SIDE OTP IS:",otp)
            utp=int(input("enter otp:"))
            if(username=="admin") and (password=="admin123")and (utp==otp):
                print("login succesful")
                print("WELCOME TO ADMIN SIDE ")
                c=0
                while(c!=5):
                    print("\t\t1.ADD NEW ACCOUNT")
                    print("\t\t2.DELETE AN ACCOUNT")
                    print("\t\t3.SEARCH AN ACCOUNT")
                    print("\t\t4.TRANSACTION ")
                    print("\t\t5.EXIT")
                    c=int(input("ENTER YOUR CHOICE :"))
                    if (c==1):
                        obj1.addAccount()
                    elif (c==2): 
                        accno=int(input("ENTER ACCOUNT  NUMBER TO DELETE :"))
                        obj1.delAccount(accno)      
                    elif (c==3): 
                        accno=int(input("ENTER ACCOUNT  NUMBER TO SEARCH :"))
                        obj1.searchAccount(accno)   
                    elif(c==4):
                        date=input("enter date (yyyy-mm--dd):")
                        obj1.transact(date)       
                    elif (c==5):
                        print("\t\t THANK YOU FOR USING ADMIN SIDE👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻") 
                    else:
                        print("wrong choice made")
                        break  
            else:
                print("please enter right username,password and otp")      
        elif(choice==2):
             username=input('enter username:')
             password=stdiomask.getpass("enter password:",mask='*')
             otp=random.randint(1000,9999)
             print("YOUR USER  SIDE OTP IS:",otp)
             utp=int(input("enter otp:"))
             if(username=="user") and (password=="user123")and (utp==otp):
                    print("login succesful")
                    print("WELCOME TO USER SIDE ")
                    ch=0
                    while(ch!=5):
                        print(" 🖥️  🖥️  🖥️   🖥️  🖥️  🖥️  🖥️  🖥️  🖥️   🖥️  🖥️  🖥️ ")
                        print("\t\t1.DISPLAY ACCOUNT BALANCE")
                        print("\t\t2.WITHDRAW AMOUNT")
                        print("\t\t3.DEPOSIT AMOUNT")
                        print("\t\t4.TRANSFER")
                        print("\t\t5.EXIT")
                        ch=int(input("ENTER YOUR CHOICE :"))
                        if (ch==1):
                            accno=int(input("ENTER ACCOUNT  NUMBER TO DISPLAY BALANCE :"))
                            obj11.displayBalance(accno)      
                        
                        elif (ch==2): 
                            accno=int(input("ENTER ACCOUNT  NUMBER :"))
                            amt=int(input("ENTER AMOUNT TO WITHDRAW :"))
                            obj11.withdrawAmount(accno,amt)      
                        elif (ch==3): 
                            accno=int(input("ENTER ACCOUNT  NUMBER :"))
                            amt1=int(input("ENTER AMOUNT TO DEPOSIT :"))
                            obj11.depAmt(accno,amt1)    
                        elif (ch==4):
                            accno1=int(input("ENTER ACCOUNT  NUMBER 1 TO  CREDIT:"))
                            accno2=int(input("ENTER ACCOUNT  NUMBER 2 TO DEBIT:"))
                            amt1=int(input("ENTER AMOUNT TO TRANSFER :"))
                            obj11.Transfer(accno1,accno2,amt1)
                            
                        elif(ch==5):
                            print("THANK YOU FOR USING OUR APPLICATION🚀")
             else:
                print("please enter right username,password and otp")             
                
        elif(choice==3):
            print("exit")
            print("🔚🔚🔚🔚🔚🔚🔚🔚🏁🏁🏁🏁🏁")
            break
