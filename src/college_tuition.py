import datetime
from .ongoing_fixed_impact import OngoingImpact


class CollegeTuition(OngoingImpact):
    PERIOD = datetime.timedelta(days=365/2)

    def _adjusted(self, date):
        return -self.yearly_amount

    def __init__(self, start, yearly_tuition) -> None:
        end = start + datetime.timedelta(days=365*4)
        super().__init__(yearly_amount=yearly_tuition,
                         start=start, end=end)
