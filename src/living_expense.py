import datetime
from .ongoing_fixed_impact import OngoingImpact


class LivingExpenses(OngoingImpact):
    PERIOD = datetime.timedelta(days=1)

    def _adjusted(self, date):
        return -self.yearly_amount
