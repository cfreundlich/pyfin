import unittest
import datetime
import src.property_tax


NOW = datetime.datetime.now().date()
YEAR = datetime.timedelta(days=365)


class PropertyTaxTestCase(unittest.TestCase):
    def test_cost(self):
        price = 2.5e6
        rate = 0.01125
        property_tax = src.property_tax.PropertyTax(
            purchase_price=2.5e6,
            closing_date=NOW,
            rate=rate
        )
        self.assertAlmostEqual(
            sum(amount for date, amount in property_tax.events()
                if date < NOW + YEAR),
            -price * rate,
            places=-3
        )
        self.assertAlmostEqual(
            sum(1 for date, _ in property_tax.events()
                if date < NOW + YEAR),
            2,
            places=0
        )
