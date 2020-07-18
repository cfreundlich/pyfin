import datetime
from .ongoing_fixed_impact import OngoingFixedImpact


class Salary(OngoingFixedImpact):
    PERIOD = datetime.timedelta(days=14)

    def __init__(self, yearly_amount, start, end, income_tax_rate=0.4) -> None:
        super().__init__(yearly_amount, start, end)
        self.income_tax_rate = income_tax_rate

    def _adjusted(self):
        return self.yearly_amount * (1 - self.income_tax_rate)
