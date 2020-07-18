import datetime
import heapq
import typing
import matplotlib.pyplot as plt
from .bank_account import BankAccount
from .impact import Impact


TODAY = datetime.datetime.now().date()


Events = typing.Dict[str, Impact]


class Sim:
    def __init__(self, bank_account: BankAccount) -> None:
        self.bank = bank_account
        self.all_events = list()

    def _add(self, events: typing.List[typing.Tuple[datetime.date, int]]):
        for event in events:
            heapq.heappush(self.all_events, event)

    def consume(self, events: Events):

        for name, source in events.items():
            new_events = source.events()
            print(f'Adding {len(new_events)} cash impacts due to {name}')
            print(f'Last is ${new_events[-1][1]} on {new_events[-1][0]}')
            self._add(new_events)

    def run(self):
        for date in (TODAY + datetime.timedelta(days=i) for i in range(365*30)):
            self.bank.appreciate(datetime.timedelta(days=1))
            while self.all_events and self.all_events[0][0] <= date:
                self.bank.add(heapq.heappop(self.all_events)[1])
            if self.bank.val < 0:
                break

    def plot(self):
        plt.plot([date for date, _ in self.bank.history],
                 [money for _, money in self.bank.history])
        plt.grid()
        plt.title('Liquid Cash Balance')
