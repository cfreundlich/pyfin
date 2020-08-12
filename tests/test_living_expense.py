import unittest
import datetime
import src.living_expense


import src.today
TODAY = src.today.today()
YEAR = datetime.timedelta(days=365)


class LivingExpenseTestCase(unittest.TestCase):
    def test_cost(self):
        living_expense = src.living_expense.LivingExpenses(
            start= TODAY,
            yearly_amount=1e5
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in living_expense.events()
                if date <  TODAY + YEAR),
            -1e5,
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in living_expense.events()
                if date <  TODAY + YEAR),
            365,
            places=0
        )
