import unittest
import datetime
import src.living_expense


NOW = datetime.datetime.now().date()
YEAR = datetime.timedelta(days=365)


class LivingExpenseTestCase(unittest.TestCase):
    def test_cost(self):
        living_expense = src.living_expense.LivingExpenses(
            start=NOW,
            yearly_amount=1e5
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in living_expense.events()
                if date < NOW + YEAR),
            -1e5,
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in living_expense.events()
                if date < NOW + YEAR),
            365,
            places=0
        )
