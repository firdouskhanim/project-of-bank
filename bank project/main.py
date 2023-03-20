import datetime as dt 
import re
import sys
from user import savings_account
from user import checking_account
from user import business_account
from user import account

class main:  
  def execute(self):    
      while True:
            print("*"*80)
            print("WelCome To Axis Bank".center(80),"\n")
            print("*"*80)
            pattern='^[0-9]{4}$'
            password=input("ENTER THE 4 PIN PASSWORD:      ")
            result=re.findall(pattern,password)
            if result:
               print("Password is Valid")
               print("*"*80)
               print("Please Select Transaction".center(80),"\n")
               print("*"*80)
               print("[1.] Deposite Balance       [2.] Balance Inquery          \n[3.] Cash Withdrawl         [4.] Exit ")
               t=dt.datetime.now()
               print(t)
               ch=int(input("Enter the Choice:    "))
               if ch==1:
                  ca=checking_account()
                  ca.deposit()
              

               if ch==2:
                  ca=checking_account()  
                  ca.check_balance()        
                     
               if ch==3:
                  print("[1.] Business Account \n[2.] Savings Account")
                  sh=int(input("Enter the Chice:   "))
                  if sh==1:
                     ba=business_account()
                     ba.withdraw()
                     ba.check_balance()
                  if sh==2:
                     sa=savings_account()
                     sa.withdraw()
                     sa.check_balance()
              
                           
               if ch==4:
                  sys.exit()   
            else:
                print("Wrong id,Please Try Again.")         
              
if __name__=="__main__":
  obj=main()
  obj.execute()
