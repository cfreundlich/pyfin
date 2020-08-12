import datetime
import logging
import heapq
import typing
import matplotlib.pyplot as plt
from .bank_account import BankAccount
from .impact import Impact

LOGGER = logging.getLogger()
import src.today
TODAY = src.today.today()

Events = typing.Dict[str, Impact]


class Sim:
    def __init__(self,
                 bank_account: BankAccount,
                 stock_market_rate_of_return=3e-2,
                 days_to_simulate=365 * 10) -> None:
        self.bank = bank_account
        self.all_events = list()
        self.stock_market_rate_of_return = stock_market_rate_of_return
        self.days_to_simulate = days_to_simulate

    def _add(self, events: typing.List[typing.Tuple[datetime.date, int]]):
        for event in events:
            heapq.heappush(self.all_events, event)

    def consume(self, events: Events):

        for name, source in events.items():
            new_events = source.events()
            LOGGER.info(f'Adding {len(new_events)} cash impacts due to {name}')
            LOGGER.info(f'Last is ${new_events[-1][1]} on {new_events[-1][0]}')
            self._add(new_events)

    def run(self):
        dates = (TODAY + datetime.timedelta(days=i)
                 for i in range(self.days_to_simulate))
        for date in dates:
            self.bank.appreciate(
                time=datetime.timedelta(days=1),
                stock_market_rate_of_return=self.stock_market_rate_of_return)
            while self.all_events and self.all_events[0][0] <= date:
                self.bank.add(heapq.heappop(self.all_events)[1])
            if self.bank.val < 0:
                break

    def plot(self, label=None):
        plt.plot([date for date, _ in self.bank.history],
                 [money for _, money in self.bank.history],
                 label=label)
