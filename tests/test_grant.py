import unittest
import datetime
import src.grants.grant
import src.today


class GrantTestCase(unittest.TestCase):

    def test_vest_dates_new_grant(self):
        grant = src.grants.grant.Grant(
            grant_date=datetime.date(year=2020, month=8, day=1),
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
        compare = zip(dates_should_be, grant.get_unvested())
        for expected, (calculated, amount) in compare:
            self.assertEqual(expected, calculated)
            self.assertEqual(1, amount)

    def test_portion_existing_grant(self):
        grant = src.grants.grant.Grant(
            grant_date=datetime.date(year=2020, month=8, day=1),
            unvested_shares=100)
        vest_dates = list(grant.get_unvested(
            after=datetime.date(year=2024, month=6, day=4)))
        self.assertEqual(len(vest_dates), 1)
        self.assertEqual(datetime.date(year=2024, month=6, day=5),
                         vest_dates[0][0])
        self.assertEqual(vest_dates[0][1], 100)
