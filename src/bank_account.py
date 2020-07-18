import datetime


class BankAccount:
    def __init__(self, val, age=None) -> None:
        self.val = val
        self.age = age if age else datetime.datetime.now().date()
        self.history = [(age, val)]

    @staticmethod
    def _daily_compound_rate(stock_market_rate_of_return):
        fraction = 1/365.25
        rate = (1 + stock_market_rate_of_return) ** fraction
        return rate - 1

    def appreciate(self, time, stock_market_rate_of_return=3e-2):
        if time < datetime.timedelta(days=1):
            Warning('Interval must be longer that a day')
            return

        if time % datetime.timedelta(days=1) != datetime.timedelta(0):
            Warning('Appreciation interval is not an exact multiple of 1 day')

        daily_rate = self._daily_compound_rate(stock_market_rate_of_return)
        self.val *= (1 + daily_rate) ** time.days
        self.age += time
        self.history += [(self.age, self.val)]

    def add(self, amount):
        self.val += amount
        if self.age == self.history[-1][0]:
            self.history[-1] = (self.age, self.val)
        else:
            self.history += [(self.age, self.val)]
