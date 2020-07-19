import datetime
import unittest
import src.mortgage


NOW = datetime.datetime.now().date()


class MortgageTestCase(unittest.TestCase):
    def test_monthly_payment(self):
        mortgage = src.mortgage.Mortgage(purchase_price=2.5e6,
                                         closing_date=NOW,
                                         downpayment_help=0,
                                         downpayment_pct=0.2,
                                         interest_rate=3.242e-2,
                                         loan_term=360)
        self.assertAlmostEqual(mortgage.events()[-1][1], -8695, places=-1)
        self.assertEqual(len(mortgage.events()), 361)

    def test_downpayment(self):
        mortgage = src.mortgage.Mortgage(purchase_price=2.5e6,
                                         closing_date=NOW,
                                         downpayment_help=0,
                                         downpayment_pct=0.2,
                                         interest_rate=3.242e-2,
                                         loan_term=360)
        self.assertAlmostEqual(mortgage.events()[0][1], -5e5, places=-1)


    def test_downpayment_help(self):
        mortgage = src.mortgage.Mortgage(purchase_price=2.5e6,
                                         closing_date=NOW,
                                         downpayment_help=1e4,
                                         downpayment_pct=0.2,
                                         interest_rate=3.242e-2,
                                         loan_term=360)
        self.assertAlmostEqual(mortgage.events()[0][1], -4.9e5, places=-1)
