import unittest
import datetime
import src.one_time_expense


NOW = datetime.datetime.now().date()


class OneTimeEventTestCase(unittest.TestCase):
    def test_single_event(self):
        event = src.one_time_expense.OneTimeExpense(when=NOW, amount=1e5)
        self.assertEqual(event.events()[-1][1], -1e5)
        self.assertEqual(event.events()[-1][0], NOW)
