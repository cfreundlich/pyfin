import datetime


class BankAccount:
    def __init__(self, val, age=None) -> None:
        self.val = val
        self.age = age if age else datetime.datetime.now().date()
        self.history = [(age, val)]

    def appreciate(self, time, stock_market_rate_of_return=3e-2):
        if time == datetime.timedelta(days=0):
            return
        ratio = time / datetime.timedelta(days=365.25)
        pct_increase = stock_market_rate_of_return * ratio
        self.val *= (1 + pct_increase)
        self.age += time
        self.history += [(self.age, self.val)]

    def add(self, amount):
        self.val += amount
        if self.age == self.history[-1][0]:
            self.history[-1] = (self.age, self.val)
        else:
            self.history += [(self.age, self.val)]
