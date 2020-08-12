import unittest
import datetime
import src.grants.grant


class GrantTestCase(unittest.TestCase):
    def test_portion(self):
        grant = src.grants.grant.Grant(grant_date=datetime.date(year=2020, month=8, day=1),
        unvested_shares=16)
        self.assertEqual(grant.portion, 1)

    def test_vest_dates(self):
        grant = src.grants.grant.Grant(grant_date=datetime.date(year=2020, month=8, day=1),
                                   unvested_shares=16)
        dates_should_be = [
            datetime.date(year=2020, month=9, day=5),
            datetime.date(year=2020, month=12, day=5),
            datetime.date(year=2021, month=3, day=5),
            datetime.date(year=2021, month=6, day=5),
            datetime.date(year=2021, month=9, day=5),
            datetime.date(year=2021, month=12, day=5),
            datetime.date(year=2022, month=3, day=5),
            datetime.date(year=2022, month=6, day=5),
            datetime.date(year=2022, month=9, day=5),
            datetime.date(year=2022, month=12, day=5),
            datetime.date(year=2023, month=3, day=5),
            datetime.date(year=2023, month=6, day=5),
            datetime.date(year=2023, month=9, day=5),
            datetime.date(year=2023, month=12, day=5),
            datetime.date(year=2024, month=3, day=5),
            datetime.date(year=2024, month=6, day=5)
        ]
        for expected, calculated in zip(dates_should_be, grant.vest_dates()):
            self.assertEqual(expected, calculated)
