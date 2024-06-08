import inspect


class Account:
    _balance = None
    _successor = None

    def set_next(self, account):
        self._successor = account

    def pay(self, amount_to_pay):
        caller_frame = inspect.stack()[1]
        caller_name = caller_frame.function
        caller_class = caller_frame.frame.f_locals.get('self', None).__class__.__name__

        if self.can_pay(amount_to_pay):
            print(f"Paid {str(amount_to_pay)} using {self.__class__.__name__} (called by {caller_name} of {caller_class}) ")
        elif self._successor:
            print(f"Cant paid {str(amount_to_pay)} using {self.__class__.__name__}, (called by {caller_name} of {caller_class})  proceeding...")
            self._successor.pay(amount_to_pay)
        else:
            raise ValueError("None of the accounts have enough balance")

    def can_pay(self, amount):
        return self._balance >= amount


class Bank(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


class Paypal(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


class Bitcoin(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


bank = Bank(100)
paypal = Paypal(200)
bitcoin = Bitcoin(300)
bank.set_next(paypal)
paypal.set_next(bitcoin)
bank.pay(259)
