import datetime
import dateutil.parser
import logging
import os
import pandas as pd
from .impact import Impact


LOGGER = logging.getLogger()
NOW = datetime.datetime.now().date()
FOUR_YEAR = datetime.timedelta(days=365.25 * 4)


class RestrictedStock(Impact):
    POSSIBLE_VEST_DAYS = [
        datetime.date(year=year, month=month, day=5)
        for year in range(NOW.year, NOW.year + 10)
        for month in [3, 6, 9, 12]
    ]

    def __init__(self, init_price, last_day=None, tax_rate=0.4) -> None:
        self.last_day = last_day
        self.init_price = init_price
        self.tax_rate = tax_rate

    def events(self):
        less_tax = (1 - self.tax_rate)
        events = [(date, self.share_price(date) * shares * less_tax)
                  for date, shares in self._vesting_schedule()]
        if self.last_day:
            return [(date, amount) for date, amount in events
                    if date < self.last_day]
        return events

    def share_price(self, future_date):
        return self.init_price

    def _read_etrade(self) -> pd.DataFrame:
        fpath = os.path.join(os.path.curdir, 'data_inputs', 'rsu.xlsx')
        xl = pd.ExcelFile(fpath)
        return xl.parse('Unvested')

    def _vesting_schedule(self):

        events = []
        for name, group in self._read_etrade().groupby('Plan Type'):
            if name != 'Rest. Stock':
                LOGGER.warning('Unrecognized plan type: %s', name)
                continue

            for _, row in group.iterrows():
                grant_day = dateutil.parser.parse(row['Grant Date']).date()
                runs_out_on = grant_day + FOUR_YEAR
                vest_dates = [day for day in self.POSSIBLE_VEST_DAYS
                              if NOW <= day <= runs_out_on]
                amount = row['Unvested Qty.'] / len(vest_dates)
                events += [(day, amount) for day in vest_dates]
        return events
