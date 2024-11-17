from time import sleep

class SBI:
    location = "bengalure"
    chairman = "ss"
    ifsc_code = "234565478654dsf5"

    def __init__(self, name, pin, accountno, balance):
        self.name = name
        self.__pin = pin
        self.account = accountno
        self.balance = balance
        self.transaction = []


    def deposite(self,amount):
        deposite = print(f"{amount}.Rs Deposited to your account")
        self.balance += amount
        self.transaction.append(f"{amount}.Rs Deposited to your account")


    def withdraw(self, amount, pin):
        if self.__pin == pin:

            
            
            if self.balance > amount:
                withdraw = print(f"{amount}.Rs withdrawed from your account")
                self.balance -= amount
                self.transaction.append(f"{amount}.Rs withdrawed from your account")
            
            else:
                print("insuffient balance")

        else:
            print("Wrong pin enter your correct pin")

    def display_transaction(self,pin):
        if self.__pin == pin:
            for transaction in self.transaction:
                print(transaction)
                sleep(1)
    @property
    def pin(self):
        print(self.__pin)

    @pin.setter
    def pin(self,new_pin):
        self.__pin = new_pin
        print(self.__pin)

    


sab = SBI("SABARISH S",2003 , 1234567, 3000)

sab.deposite(500)

sab.deposite(500)

sab.deposite(1000)

print(sab.name)

print(sab.balance)

sab.withdraw(3000, 2003)

print(sab._SBI__pin)

print(sab.balance)

sab.display_transaction(2003)

sab.pin

sab.pin = 4455

sab.withdraw(200,2003)
sab.withdraw(200,4455)



    












