import datetime
from .ongoing_fixed_impact import OngoingFixedImpact


class CollegeTuition(OngoingFixedImpact):
    PERIOD = datetime.timedelta(days=30*6)

    def _adjusted(self):
        return -self.yearly_amount

    def __init__(self, start, yearly_tuition) -> None:
        end = start + datetime.timedelta(days=365*4)
        super().__init__(yearly_amount=yearly_tuition,
                         start=start, end=end)
