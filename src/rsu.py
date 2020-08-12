import datetime
import logging
from .impact import Impact
import src.grants.etrade

LOGGER = logging.getLogger()
NOW = datetime.datetime.now().date()


class RestrictedStock(Impact):
    def __init__(self, init_price, last_day=None, tax_rate=0.4) -> None:
        self.last_day = last_day
        self.init_price = init_price
        self.tax_rate = tax_rate

    def events(self):
        less_tax = (1 - self.tax_rate)
        events = [(date, self.share_price(date) * shares * less_tax)
                  for date, shares in self._rsu_events()]
        if self.last_day:
            return [(date, amount) for date, amount in events
                    if date < self.last_day]
        return events

    def share_price(self, future_date):
        return self.init_price

    @staticmethod
    def _rsu_events():
        return [(day, grant.portion) for grant in src.grants.etrade.read()
                for day in grant.vest_dates()]
