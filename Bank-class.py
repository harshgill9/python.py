from datetime import datetime 

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.__history = []
        self.filePath = f"logs{name}.txt"
    def deposit(self): 
        amount = int(input(f"Enter the deposit amount for {self.name} : "))
        self.__balance += amount
        print(f"Deposited: {amount}")
        
        transaction = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Deposited {amount}"
        self.__history.append(f"Deposited: {amount}")
        self.__history.append(transaction)
        with open (self.filePath, "a") as logs:
            logs.write(transaction + "\n")
        
       
    def withdraw(self,):
        amount = int(input(f"Enter your withdraw amount {self.name} : "))
        if  amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            transaction = f"Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} --> Withdrawn: {amount}"
            self.__history.append(transaction)
            with open (self.filePath, "a") as logs:
                logs.write(transaction + "\n")

    def get_balance(self):
        return self.__balance
    
    def get_history(self):
        print(f"Transaction History: {self.name}")
        # for entry in self.__history:
        #     print(entry)
        with open (self.filePath, "r") as logs:
            for line in logs:
                print(line.strip())

    def transfer(self, reciver):
        amount = int(input(f"enter the transfer amount {reciver.name} : "))
        if (amount > self.__balance):
            print(f"Insufficient balance! {self.name}")
        else:
            self.__balance -= amount
            reciver.__balance += amount
            
            transaction_out = f"date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> Transfered {amount} Transferred to {reciver.name}"
            transaction_in = f"date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> Received {amount} from {self.name}"
            self.__history.append(transaction_out)
            reciver.__history.append(transaction_in)
            with open (self.filePath, "a") as logs:
                logs.write(transaction_out + "\n")
            with open (reciver.filePath, "a") as logs:
                logs.write(transaction_in + "\n")

c1 = Bank("Harsh", 1000)
c2 = Bank("Gill", 2000)

c1.deposit()
c1.withdraw()
# c2.deposit()

c1.transfer(c2)

print(c1.get_balance())
print(c2.get_balance())

c1.get_history()
c2.get_history()

