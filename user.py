from account import Account
from exp import WrongOperation
import datetime
class User():
    def displayBalance(self,accno):
         with open("accountdetails.txt","r") as fp:
                for e in fp:
                    try:
                        e.index(str(accno),0,4)
                        print("-----------------------------------------------")
                        print("ACCOUNT FOUND 🧾🧾")
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

    def withdrawAmount(self,accno,amt) :
            container = []
            found = False
            with open("accountdetails.txt","r") as fp:
                for e in fp:
                    sep_list = e.split(",")
                    if(sep_list[0] == str(accno)):
                        found =True
                        print("----------- ACCOUNT DETAIL---------------------")
                        print("ACCOUNT  NO        IS          :",sep_list[0])
                        print("CURRENT ACCOUNT  BALANCE   IS  :",sep_list[3])
                        cur=int(sep_list[3])
                        try:
                            if cur<amt:
                                #print("❌❌Insufficient balance you only have ❌❌ Rs",cur)
                                e = ','.join(sep_list)
                                raise WrongOperation("INSUFFICIENT BALANCE")
                            # return
                        except  WrongOperation as ex:
                            print(ex)
                        else:    
                            cur=cur-amt
                            sep_list[3]=str(cur)
                            print("AMOUNT WITHDRAW SUCCESFUL💷💷")
                            e = ','.join(sep_list)
                    
                    container.append(e)

            if(found ==True):
                with open("accountdetails.txt", 'w') as fp:
                    for x in container:
                        fp.write(x)
                        #fp.write("\n")
            else:
                print("ACCOUNT NOT FOUND")




                                            
            with open("transaction.txt", "a") as fp:
                for e in container:
                    splist=["","db",str(datetime.datetime.now())]
                #      fp.write(e)
                #      fp.write(",")
                #      fp.write("db")
                #      fp.write(",")
                #      fp.write(str(datetime.datetime.now()))
                #      fp.write("\n")
                # self.displayBalance(accno)    
                    sep_list1 = e.split(",")
                    if(sep_list1[0] == str(accno)):

                        a1= ','.join(sep_list1)
                        #a=str((sep_list1[0]),(sep_list1[1]),(sep_list1[2]),(sep_list1[3],"db",datetime.datetime.now))+"\n"
                        a2=','.join(splist)
                        fp.write(str(a1))
                        fp.write(str(a2))
                        fp.write("\n")
                        fp.write("\n")
                self.displayBalance(accno)    

                     
        
        
    def depAmt(self,accno,amt) :
         #container=[]
         #f=False
        #  with open("accountdetails.txt","r") as fp:
        #         for e in fp:
        #             try:
                        
                          
        #                     e.index(str(accno),0,4)
        #                     print("-----------------------------------------------")
        #                     f=True
        #                     print("ACCOUNT FOUND")
        #                     list2=e.split(",")
        #                     print("----------- ACCOUNT DETAIL---------------------")
        #                     print("ACCOUNT  NO        IS  :",list2[0])
        #                     print(" CURRENT ACCOUNT  BALANCE   IS  :",list2[3])
        #                     print("-----------------------------------------------")
        #                     #bal=list2[3]
        #                     #print(bal)
                            
        #                     cur=int(list2[3])
        #                     cur=cur+amt
        #                     list2[3]=str(cur)
        #                     print("AMOUNT DEPOSIT SUCCESFUL")
        #                     e = ','.join(list2)
        #                     container.append(e)
        #                     print(e)
        #                     break
        #             except ValueError:
        #                     pass
        #  if(f==True):
        #     with open("accountdetails.txt", 'w') as fp:
        #         for x in container:
        #             fp.write(x)


        #  else:
        #     print("ACCOUNT NOT FOUND")
        #     print("--------------------------")
        container = []
        found = False
        with open("accountdetails.txt","r") as fp:
            for e in fp:
                sep_list = e.split(",")
                if(sep_list[0] == str(accno)):
                    found =True
                    print("----------- ACCOUNT DETAIL---------------------")
                    print("ACCOUNT  NO        IS          :",sep_list[0])
                    print("CURRENT ACCOUNT  BALANCE   IS  :",sep_list[3])
                    cur=int(sep_list[3])
                    cur=cur+amt
                    sep_list[3]=str(cur)
                    print("AMOUNT DEPOSIT SUCCESFUL💲💲💲")
                    
                    
                    e = ','.join(sep_list)
                
                container.append(e)

        if(found ==True):
            with open("accountdetails.txt", 'w') as fp:
                for x in container:
                    fp.write(x)
                    fp.write("\n")
        else:
            print("ACCOUNT NOT FOUND")




                                        
        with open("transaction.txt","a") as fp:
            for e in container:
                    splist=["","cr",str(datetime.datetime.now())]
                    sep_list1 = e.split(",")
                    if(sep_list1[0] == str(accno)):

                        a1= ','.join(sep_list1)
                        #a=str((sep_list1[0]),(sep_list1[1]),(sep_list1[2]),(sep_list1[3],"db",datetime.datetime.now))+"\n"
                        a2=','.join(splist)
                        fp.write(str(a1))
                        fp.write(str(a2))
                        fp.write("\n")
                        fp.write("\n")
            self.displayBalance(accno) 
                   

    def Transfer(self,acc1,acc2,amt):
            container = []
            found = False
            with open("accountdetails.txt","r") as fp:
                    for e in fp:
                        sep_list = e.split(",")
                        if(sep_list[0] == str(acc1)):
                            found =True
                            print("----------- ACCOUNT DETAIL---------------------")
                            print("ACCOUNT  NO        IS  :",sep_list[0])
                            print(" CURRENT ACCOUNT  BALANCE   IS  :",sep_list[3])
                            cur=int(sep_list[3])
                            cur=cur-amt
                            sep_list[3]=str(cur)
                            print("AMOUNT TRANSEFERRED SUCCESFUL 💳💳")
                            
                            
                            e = ','.join(sep_list)
                        
                        container.append(e)

            if(found ==True):
                    with open("accountdetails.txt", 'w') as fp:
                        for x in container:
                            fp.write(x)
                            fp.write("\n")
            else:
                 print("ACCOUNT NOT FOUND")




                                                
            with open("transaction.txt","a") as fp:
                for e in container: 
                    splist=["","db",str(datetime.datetime.now())]
                    sep_list1 = e.split(",")
                    if(sep_list1[0] == str(acc1)):

                        a1= ','.join(sep_list1)
                        #a=str((sep_list1[0]),(sep_list1[1]),(sep_list1[2]),(sep_list1[3],"db",datetime.datetime.now))+"\n"
                        a2=','.join(splist)
                        fp.write(str(a1))
                        fp.write(str(a2))
                        fp.write("\n")
                        fp.write("\n")
            self.displayBalance(acc1)    
            


            container = []
            found = False
            with open("accountdetails.txt","r") as fp:
                for e in fp:
                    sep_list = e.split(",")
                    if(sep_list[0] == str(acc2)):
                        found =True
                        print("----------- ACCOUNT DETAIL---------------------")
                        print("ACCOUNT  NO        IS  :",sep_list[0])
                        print(" CURRENT ACCOUNT  BALANCE   IS  :",sep_list[3])
                        cur=int(sep_list[3])
                        cur=cur+amt
                        sep_list[3]=str(cur)
                        print("AMOUNT RECEIVED SUCCESFUL 💵💵")
                        
                        
                        e = ','.join(sep_list)
                    
                    container.append(e)

            if(found ==True):
                with open("accountdetails.txt", 'w') as fp:
                    for x in container:
                        fp.write(x)
                    fp.write("\n")
            else:
                print("ACCOUNT NOT FOUND")




                                        
            with open("transaction.txt","a") as fp:
                       for e in container:
                        splist=["","cr",str(datetime.datetime.now())]
                        sep_list1 = e.split(",")
                        if(sep_list1[0] == str(acc2)):

                            a1= ','.join(sep_list1)
                            #a=str((sep_list1[0]),(sep_list1[1]),(sep_list1[2]),(sep_list1[3],"db",datetime.datetime.now))+"\n"
                            a2=','.join(splist)
                            fp.write(str(a1))
                            fp.write(str(a2))
                            fp.write("\n")
                            fp.write("\n")
            self.displayBalance(acc2)   
                
                                                     