class Bankaccount:        
    def __init__(self, int_rate, balance):
        self.int_rate = .01
        self.balance = 1000

    # deposit method
    def deposit(self, amount):   
        self.balance += amount   
    
    # withdrawal method
    def withdrawal(self, amount):
        self.balance -= amount

    # interest rate
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        else:
            print("Insufficient Funds: Charging a $5 fee")
    # display balance
    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest rate: {self.int_rate}")
    
#________________________________________________________
class User:        
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bankaccount(int_rate=0.02, balance=0)

    # deposit method
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account.deposit(amount)    # self.account_balance += amount

    # withdrawal method
    def make_withdrawal(self, amount):
        self.account.withdrawal(100)     #self.account_balance -= amount

    # display balance
    def display_user_balance(self):        #display_user_balance(self):
        self.account.display_account_info()
        print(f"User: {self.name}, Balance: ${self.account.balance}")    # print(f"User: {self.name}, Balance: ${self.account.balance}")
    
rick = User("rick", "rick@dojo.com") # User

rick.make_deposit(100)      #make_deposit
rick.make_deposit(100)
rick.make_deposit(100)
rick.make_withdrawal(50)
rick.display_user_balance()