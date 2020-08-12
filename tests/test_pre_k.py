import unittest
import datetime
import src.pre_k


import src.today
TODAY = src.today.today()
YEAR = datetime.timedelta(days=365)


class PreKTestCase(unittest.TestCase):
    def test_cost(self):
        pre_k = src.pre_k.PreK(
            start= TODAY,
            yearly_amount=1e4,
            end= TODAY+YEAR
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in pre_k.events()
                if date <  TODAY + YEAR),
            -1e4,
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in pre_k.events()
                if date <  TODAY + YEAR),
            26,
            places=0
        )
