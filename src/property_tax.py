import datetime
from .ongoing_fixed_impact import OngoingImpact


class PropertyTax(OngoingImpact):
    PERIOD = datetime.timedelta(days=365 / 2)

    def __init__(self, purchase_price, closing_date, rate=0.01125) -> None:
        super().__init__(yearly_amount=purchase_price * rate,
                         start=closing_date)

    def _adjusted(self, date):
        return -self.yearly_amount
