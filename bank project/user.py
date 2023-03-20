from abc import ABC,abstractmethod
import json as js
class account(ABC):
  def __init__(self):
     

   @abstractmethod   
   def deposite(self):
      pass

  @abstractmethod      
  def withdraw(self):
       pass  
  
  @abstractmethod      
  def check_balance(self):
      pass

class checking_account(account):
  def __init__(self):
      super().__init__()
      self.balance=0
      self.row={}


  def deposit(self):
      amount=int(input("ENTER THE AMOUNT TO DEPOSITE:    ")) 
      self.balance += amount
      self.row={"101":self.balance} 
      f=open("balance.json","w")
      js.dump(self.row,f)
      f.close()       

  def withdraw(self):
      amount=int(input("ENTER THE AMOUNT TO WITHDRAWL:    ")) 
      if amount <= self.balance:
         self.balance -= amount
         print(f"Withdrawl successful.Your new balance is ${self.balance}")
      else:
         print("Insufficient balance.Withdrawl failed.")    
       

  def check_balance(self):
      f=open("balance.json")
      r=js.load(f)
      for i,j in r.items():
          print(f"your Current balance is ${j}")

    
                     
class savings_account(account):
  def __init__(self):
      super().__init__()
      self.balance=5000
      self.data={}

  def deposit(self):
      amount=int(input("ENTER THE AMOUNT TO DEPOSITE:    ")) 
      self.balance+=amount
      print(f"Deposit successful.Your new balance is ${self.balance}")
       
  def withdraw(self):
      f=open("balance.json")
      r=js.load(f)
      for i,j in r.items():
          amount=int(input("ENTER THE AMOUNT TO WITHDRAWL:    ")) 
          if amount <= j:
             j -= amount
             print(f"Withdrawl successful.Your new balance is ${j}")
          else:
             print("Insufficient balance.Withdrawl failed.")
      self.data={"102":j}
      f=open("data.json","w")
      js.dump(self.data,f)
      f.close() 


  def check_balance(self):
      f=open("data.json")
      r=js.load(f)
      for i,j in r.items():
          print(f"your Current account balance is ${j}")       

  
class business_account(account):
  def __init__(self):
      super().__init__()
      self.balance=5000
      self.show={}

  def deposit(self):
      amount=int(input("ENTER THE AMOUNT TO DEPOSITE:    ")) 
      self.balance+=amount
      print(f"Deposit successful.Your new balance is ${self.balance}")
       
  def withdraw(self):
      f=open("balance.json")
      r=js.load(f)
      for i,j in r.items():
          amount=int(input("ENTER THE AMOUNT TO WITHDRAWL:    ")) 
          if amount <= j:
             j -= amount
             print(f"Withdrawl successful.Your new balance is ${j}")
          else:
             print("Insufficient balance.Withdrawl failed.")

      self.show={"105":j}
      f=open("show.json","w")
      js.dump(self.show,f)
      f.close() 

       


  def check_balance(self):
      f=open("show.json")
      r=js.load(f)
      for i,j in r.items():
          print(f"your Current account balance is ${j}")       
