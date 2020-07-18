import datetime
from .ongoing_fixed_impact import OngoingFixedImpact


class LivingExpenses(OngoingFixedImpact):
    PERIOD = datetime.timedelta(days=1)

    def _adjusted(self):
        return -self.yearly_amount
