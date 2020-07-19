import datetime
from .ongoing_fixed_impact import OngoingImpact


class PreK(OngoingImpact):
    PERIOD = datetime.timedelta(days=14)

    def _adjusted(self, date):
        return -self.yearly_amount
