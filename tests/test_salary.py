import unittest
import datetime
import src.salary


NOW = datetime.datetime.now().date()
YEAR = datetime.timedelta(days=365)


class SalaryTestCase(unittest.TestCase):
    def test_cost(self):
        salary = src.salary.Salary(
            yearly_amount=1e5,
            start=NOW,
            end=NOW + YEAR
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in salary.events()
                if date < NOW + YEAR),
            1e5 * (1 - salary.income_tax_rate),
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in salary.events()
                if date < NOW + YEAR),
            26,
            places=0
        )
