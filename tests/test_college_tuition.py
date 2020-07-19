import unittest
import datetime
import src.college_tuition


NOW = datetime.datetime.now().date()
YEAR = datetime.timedelta(days=365)


class CollegeTuitionTestCase(unittest.TestCase):
    def test_cost(self):
        college_tuition = src.college_tuition.CollegeTuition(
            start=NOW,
            yearly_tuition=1e5
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in college_tuition.events()
                if date < NOW + YEAR),
            -1e5,
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in college_tuition.events()
                if date < NOW + YEAR),
            2,
            places=0
        )
