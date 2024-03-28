class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Balans popolnen na {money}. Teper u tebya {self.balance}')

    def trata(self, money):
        if money > self.balance:
            print('Deneg netu')
        elif money < self.balance:
            self.balance -= money
            print(f'Spisano {money}, ostalos {self.balance}')

    def all_balance(self):
        print(f'U tebya {self.balance} babla')


babai = Account(1001, 500)
#masai = Account(1002)

babai.all_balance()
babai.deposit(500)
babai.trata(100)
#masai.all_balance()
#masai.trata(100)


