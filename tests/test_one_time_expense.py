import unittest
import datetime
import src.one_time_expense


import src.today
TODAY = src.today.today()


class OneTimeEventTestCase(unittest.TestCase):
    def test_single_event(self):
        event = src.one_time_expense.OneTimeExpense(when= TODAY, amount=1e5)
        self.assertEqual(event.events()[-1][1], -1e5)
        self.assertEqual(event.events()[-1][0],  TODAY)
