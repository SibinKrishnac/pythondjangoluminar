from datetime import datetime
class bank:
    bank_name="sbi"
    def creat_account(self,acno,person_name,balance):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance
        # self.bankname=bankname
    def deposit(self,amount):
        self.balance+=amount
        print(bank.bank_name,"your account number",self.acno,"has been credited with amount",amount,"on",datetime.today(),"available balance is",self.balance)
    def withdrawel(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(bank.bank_name,"your account number",self.acno,"has been debited with amount",amount,"on",datetime.today(),"available balance is",self.balance)
        else:
            print("transaction cancelled")
    def balance_enq(self):
        print("Your available balance is",self.balance)
        
obj=bank()
obj.creat_account(1000,"sibin",3000)
obj.deposit(10000)
obj.withdrawel(300)
obj.balance_enq()
