#try to make banking software
from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0

class savingAccount(Account):
    def __init__(self):
        #[key][0] => name ; [key][1] +> balance
        self.savingAccounts= {}
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 999999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation has been succesful. Your account number is: ", self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Sucessful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficeint balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was succesful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was succesful.")
        self.displayBalance()

    def displayBalance(self):
        print("Available balance: ", self.savingAccounts[self.accountNumber][1])

savingAccount = savingAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to Exit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingAccount.createAccount(name, deposit)
    if userChoice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous screen")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter winthdrawal amount")
                    withdrawalAmount = int(input())
                    savingAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingAccount.displayBalance()
                elif userChoice is 4:
                    break
    if userChoice is 3:
        quit()
