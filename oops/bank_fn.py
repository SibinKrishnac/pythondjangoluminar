class bank:
    def bal_enq(self):
        print("bal enq")
    def withdraw(self):
        print("withdraw")
    def __deposit(self): # we can hide any method using __
        print("deposit")
    def de_call(self):
        self.__deposit()
obj=bank()
obj.bal_enq()
obj.withdraw()
# obj.de_call()
obj._bank__deposit()
#=======
class Atm(bank):
    pass
atm=Atm()
atm.bal_enq()
atm.withdraw()
atm.de_call()