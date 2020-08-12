import datetime
import typing
import src.today


class Grant:
    VEST_MONTHS = [3, 6, 9, 12]
    VEST_DAY = 5

    def __init__(self,
                 grant_date,
                 unvested_shares,
                 schedule='quarterly',
                 duration_years=4) -> None:
        self.unvested_shares = unvested_shares
        self.schedule = schedule
        self.duration_years = duration_years

    @property
    def portion(self) -> float:
        # using fractional shares as an approximation
        return self.unvested_shares / self._n_equal_vests

    @property
    def _n_equal_vests(self) -> int:
        if self.schedule == 'quarterly':
            return 4 * self.duration_years
        raise NotImplementedError

    def _vest_day(self, year, month) -> datetime.date:
        return datetime.date(year=year, month=month, day=self.VEST_DAY)

    def _first_vest(self) -> datetime.date:
        years = [src.today.today().year + i for i in [0, 1]]
        return next(
            self._vest_day(year=y, month=m) for y in years
            for m in self.VEST_MONTHS
            if self._vest_day(year=y, month=m) > src.today.today())

    def _next_vest(self, year: int, month: int) -> datetime.date:
        current_month_index = next(i for i, m in enumerate(self.VEST_MONTHS)
                                   if m == month)

        is_last_month = current_month_index + 1 == len(self.VEST_MONTHS)
        new_year = year + 1 if is_last_month else year

        new_month_index = (current_month_index + 1) % len(self.VEST_MONTHS)
        new_month = self.VEST_MONTHS[new_month_index]

        return self._vest_day(year=new_year, month=new_month)

    def vest_dates(self) -> typing.Iterable[datetime.date]:
        vest = self._first_vest()
        yield vest
        for _ in range(self._n_equal_vests - 1):
            new_vest = self._next_vest(vest.year, vest.month)
            vest = new_vest
            yield new_vest
