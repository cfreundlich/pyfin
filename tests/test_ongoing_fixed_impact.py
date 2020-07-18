import datetime
import unittest
import src.ongoing_fixed_impact


class OngoingFixedImpactTest(unittest.TestCase):
    def test_start_new_years(self):
        impact = src.ongoing_fixed_impact.OngoingFixedImpact(
            yearly_amount=1e5,
            start=datetime.date(year=2020, month=1, day=1),
            end=datetime.date(year=2021, month=1, day=1)
        )
        self.assertAlmostEqual(
            sum(a for _, a in impact.events()),
            1e5,
            places=-3
        )

    def test_start_July(self):
        impact = src.ongoing_fixed_impact.OngoingFixedImpact(
            yearly_amount=1e5,
            start=datetime.date(year=2020, month=7, day=1),
            end=datetime.date(year=2021, month=1, day=1)
        )
        self.assertAlmostEqual(
            sum(a for _, a in impact.events()),
            1e5 / 2,
            places=-3
        )

    def test_two_years(self):
        impact = src.ongoing_fixed_impact.OngoingFixedImpact(
            yearly_amount=1e5,
            start=datetime.date(year=2020, month=1, day=1),
            end=datetime.date(year=2022, month=1, day=1)
        )
        self.assertAlmostEqual(
            sum(a for _, a in impact.events()),
            2e5,
            places=-3
        )
