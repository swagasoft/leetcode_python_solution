class CreditCard:
    def __init__(self, customer, bank, account, limit) -> None:


        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0
        

        def get_customer(self):
            return self._customer

        def get_bank(self):
            return self._bank

        def get_account(self):
            return self._account

        def charge(self, price):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True

        def make_payment(self, amount):
            self._balance  -= amount


cc = CreditCard("simon jerry", 'Zenith bank', '1012831283', '50000')
