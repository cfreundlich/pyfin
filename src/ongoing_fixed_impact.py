import datetime
from .impact import Impact

YEAR = datetime.timedelta(days=365)
TODAY = datetime.datetime.now().date()
DEAD = datetime.date(day=1, month=1, year=2088)


class OngoingImpact(Impact):
    PERIOD = datetime.timedelta(days=1)

    def __init__(self, yearly_amount, start=TODAY, end=DEAD) -> None:
        self.start = start
        self.end = end
        self.yearly_amount = yearly_amount

    def _divided_up(self):
        return self.PERIOD / YEAR

    def events(self):
        return [(date, self._amount(date)) for date in self._event_days()]

    def _amount(self, date):
        return round(self._adjusted(date) * self._divided_up())

    def _adjusted(self, date):
        return self.yearly_amount

    def _n_events(self):
        return max(round((self.end - self.start) / self.PERIOD), 0)

    def _event_days(self):
        return [self.start + i * self.PERIOD for i in range(self._n_events())]
