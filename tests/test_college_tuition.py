import unittest
import datetime
import src.college_tuition


import src.today
TODAY = src.today.today()
YEAR = datetime.timedelta(days=365)


class CollegeTuitionTestCase(unittest.TestCase):
    def test_cost(self):
        college_tuition = src.college_tuition.CollegeTuition(
            start= TODAY,
            yearly_tuition=1e5
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in college_tuition.events()
                if date <  TODAY + YEAR),
            -1e5,
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in college_tuition.events()
                if date <  TODAY + YEAR),
            2,
            places=0
        )
