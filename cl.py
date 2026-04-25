
from datetime import datetime
#self._email.  making it private     protected
#self.__password. impossible to access the variable    private 
class User:
  def __init__(self, name, email, password):
    self.name = name
    self._email = email
    self.__password = password



  def get_email(self):
    print(f"Email accessed at {datetime.now()}")
    return self._email

  @property   #Python way for a gettter
  def email(self):
    print(f"Email accesed at {datetime.now()}")
    return self._email
  
  def set_email(self, new_email):
    if "@" in new_email:
      self._email = new_email
    else:
      raise TypeError("Invalid Error")
    
  @email.setter  #python way of a setter
  def email(self, new_email):
    if "@" in new_email:
      self._email = new_email



  def get_password(self):
    return self.__password
  
user4 = User("Jane", "jane@example.com", "pass123")
print(user4.get_password())
user4.set_email("janedoe@company.com")
print(user4.get_email())
print(user4.email) #python way for a getter

#Capitilize constants. VAR
# raturn 0 <= rate <= 5.  returns true if greater than or equals to 0 and less than or equals to 5

class Bank:
  MIN_BALANCE = 100
  def __init__(self, name, amount, balance):
    self.name = name
    self.amount = amount
    self._balance = balance

  def deposit(self, amount):
    if self._is_valid_amount(amount):
      self._balance += amount
    else:
      raise ValueError("Deposit amount should be positive")
    
  def _is_valid_amount( self, amount):
    return self.amount > 0
  
  def __log_transaction(self, amount):
    print(f"Logging trannsaction of amount: {amount} at {datetime.now()}")


#Encapsulation
class BadBank:
  def __init__(self, balance):
    self.balance = balance

account = BadBank(1000)
account.balance = 300
print(account.balance)

class GoodBank:  #no setter, should not change the balace directly
  def __init__(self):
    self._balance = 1000

  @property
  def balance(self):
    return self._balance
  
  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Insufficient funds")
    self._balance += amount
  
  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Invalid amount")
    if amount > self._balance:
      raise ValueError("Insufficient funds")
    self._balance -= amount

account1 = GoodBank()
print(account1.balance)
account1.deposit(5030)
print(account1.balance)
account1.withdraw(4732)
print(account1.balance)

