import datetime
from .impact import Impact


class Mortgage(Impact):
    def __init__(self, purchase_price, closing_date, downpayment_help=0,
                 downpayment_pct=0.2, interest_rate=3e-2,
                 loan_term=360) -> None:
        self.purchase_price = purchase_price
        self.downpayment_help = downpayment_help
        self.downpayment_pct = downpayment_pct
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.closing_date = closing_date

        print(f'Borrowing ${round(self.loan_amount/1e6, 3)}M')
        print(f'Monthly mortgage payment is ${self._monthly()}')

    @property
    def loan_amount(self):
        return self.purchase_price * (1 - self.downpayment_pct)

    @property
    def monthly_interest_rate(self):
        return self.interest_rate / 12

    @property
    def first_payment(self):
        return self.closing_date + datetime.timedelta(days=60)

    def _payment_dates(self):
        return [self.first_payment + datetime.timedelta(days=30*i)
                for i in range(self.loan_term)]

    def _monthly(self):
        scale = (1 + self.monthly_interest_rate) ** self.loan_term
        denominator = scale - 1
        numerator = self.monthly_interest_rate * self.loan_amount * scale
        return round(numerator / denominator)

    def _downpayment_event(self):
        leftover = self.purchase_price * self.downpayment_pct
        leftover -= self.downpayment_help
        if leftover < 0:
            Warning('Downpayment help is larger that downpayment amount')
        if leftover > 0:
            print(f'Need to supply ${round(leftover/1e3)}k for downpayment')
        return self.closing_date, -leftover

    def events(self):
        monthly_payment = self._monthly()
        monthlies = [(date, -monthly_payment) for date in self._payment_dates()]
        return [self._downpayment_event()] + monthlies
