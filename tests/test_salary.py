import unittest
import datetime
import src.salary


import src.today
TODAY = src.today.today()
YEAR = datetime.timedelta(days=365)


class SalaryTestCase(unittest.TestCase):
    def test_cost(self):
        salary = src.salary.Salary(
            yearly_amount=1e5,
            start= TODAY,
            end= TODAY + YEAR
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in salary.events()
                if date <  TODAY + YEAR),
            1e5 * (1 - salary.income_tax_rate),
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in salary.events()
                if date <  TODAY + YEAR),
            26,
            places=0
        )

    def test_wage_growth(self):
        salary = src.salary.Salary(
            yearly_amount=1e5,
            start= TODAY,
            end= TODAY + 2*YEAR,
            yearly_wage_growth=1e-1
        )
        self.assertAlmostEqual(salary.events()[-1][1],
                               1.1 * salary.events()[0][1],
                               places=-1)
