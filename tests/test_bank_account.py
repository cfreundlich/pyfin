import datetime
import unittest
import src.bank_account


class BankAccountTestCase(unittest.TestCase):
    def test_appreciate_one_year(self):
        now = datetime.datetime.now().date()
        a_year = datetime.timedelta(days=365.25)
        val = 1e5
        rate = 0.1
        bank_account = src.bank_account.BankAccount(val=val, age=now)
        for _ in range(365):
            bank_account.appreciate(time=datetime.timedelta(days=1),
                                    stock_market_rate_of_return=rate)
        bank_account.appreciate(time=datetime.timedelta(days=0.25),
                                stock_market_rate_of_return=rate)
        self.assertAlmostEqual(bank_account.val, (1+rate)*val, places=-2)
        self.assertEqual(bank_account.age, now + a_year)

    def test_appreciate_half_year(self):
        now = datetime.datetime.now().date()
        half_year = datetime.timedelta(days=365.25/2)
        bank_account = src.bank_account.BankAccount(
            val=1e5, age=now)
        bank_account.appreciate(time=half_year,
                                stock_market_rate_of_return=0.1)
        self.assertAlmostEqual(bank_account.val, 1.05*1e5, places=-3)
        self.assertEqual(bank_account.age, now + half_year)
