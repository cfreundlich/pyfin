import datetime
from .ongoing_fixed_impact import OngoingFixedImpact


class PreK(OngoingFixedImpact):
    PERIOD = datetime.timedelta(days=14)

    def _adjusted(self):
        return -self.yearly_amount
