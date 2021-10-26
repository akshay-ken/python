class Bank:
    def __init__(self,initial_amount = 0.00):
        self.balance = initial_amount

    def log_transaction(self,log):
        with open('log.txt','a') as file:
            file.write(f'{log}\n')

    def withdrawal(self,amount):
        amount = float(amount)
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(amount)

    def deposit(self,amount):
        amount = float(amount)
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(amount)
account = Bank(100)
while True:
    try:
        action = input('0 for withdrawal and 1 for deposit : ')
    except KeyboardInterrupt:
        print(f'\n exiting \n')
        break
    if action in ['0','1']:
        if action == '0':
            amount = input('Enter amount to withdraw: ')
            account.withdrawal(amount)
        else:
            amount = input('enter amount to be Desposited: ')
            account.deposit(amount)

        print(f'remaining balance: {account.balance}')
    else:
        print('invalid action')
