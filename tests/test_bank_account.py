import datetime
import unittest
import src.bank_account


import src.today
TODAY = src.today.today()


class BankAccountTestCase(unittest.TestCase):
    def test_appreciate_one_year(self):
        a_year = datetime.timedelta(days=365.25)
        val = 1e5
        rate = 0.1
        bank_account = src.bank_account.BankAccount(val=val, age= TODAY)
        for _ in range(365):
            bank_account.appreciate(time=datetime.timedelta(days=1),
                                    stock_market_rate_of_return=rate)
        bank_account.appreciate(time=datetime.timedelta(days=0.25),
                                stock_market_rate_of_return=rate)
        self.assertAlmostEqual(bank_account.val, (1+rate)*val, places=-2)
        self.assertEqual(bank_account.age,  TODAY + a_year)

    def test_appreciate_half_year(self):
        half_year = datetime.timedelta(days=365.25/2)
        bank_account = src.bank_account.BankAccount(
            val=1e5, age= TODAY)
        bank_account.appreciate(time=half_year,
                                stock_market_rate_of_return=0.1)
        self.assertAlmostEqual(bank_account.val, 1.05*1e5, places=-3)
        self.assertEqual(bank_account.age,  TODAY + half_year)

    def test_history(self):
        bank_account = src.bank_account.BankAccount(val=0, age= TODAY)
        bank_account.appreciate(time=datetime.timedelta(days=1))
        bank_account.appreciate(time=datetime.timedelta(days=1))
        bank_account.add(1e3)
        self.assertEqual(len(bank_account.history), 3)
        self.assertGreater(bank_account.history[-1][1],
                           bank_account.history[0][1])
        self.assertGreater(bank_account.history[-1][0],
                           bank_account.history[0][0])
        self.assertEqual(bank_account.history[0][1], 0)
        self.assertEqual(bank_account.history[-1][1], 1e3)
