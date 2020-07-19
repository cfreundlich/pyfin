import datetime
from .ongoing_fixed_impact import OngoingImpact


YEAR = datetime.timedelta(days=365.25)


class Salary(OngoingImpact):
    PERIOD = datetime.timedelta(days=14)

    def __init__(self, yearly_amount, start, end, income_tax_rate=0.4,
                 yearly_wage_growth=3e-2) -> None:
        super().__init__(yearly_amount, start, end)
        self.income_tax_rate = income_tax_rate
        self.yearly_wage_growth = yearly_wage_growth

    def _years_in_role(self, date):
        return (date - self.start).days // 365

    def _adjusted(self, date):
        growth = (1 + self.yearly_wage_growth) ** self._years_in_role(date)
        wage = self.yearly_amount * growth
        return wage * (1 - self.income_tax_rate)
