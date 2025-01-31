class Atm:

    def __init__(self):

        self.__pin = ""
        self.__balance = 0

        self.__menu()

    def __menu(self):

        user_input = input(""" 
              Hello! So what you gonna do?
              1. Enter 1 to set the pin
              2. Enter 2 for depositing money
              3. Enter 3 for withdrawing money
              4. Enter 4 to check balance
              5. Enter 5 to exit                                                    
                           """)   

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit_amt()
        elif user_input == "3":
            self.withdraw_amt()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Create Pin")
        print("Pin set successfully")

    def deposit_amt(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("Deposit Successful")
        else:
            print("invalid pin!!")    

    def withdraw_amt(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.__balance = self.__balance - amount
                print("Withdraw Successful")
            else:
                print("Insufficient balance")    
        else:
            print("invalid pin!!")    
    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin!!")   


