import unittest
from unittest.mock import patch
import datetime
import src.rsu
import src.grants.etrade
import src.grants.grant


import src.today
TODAY = src.today.today()


class RSUTestCase(unittest.TestCase):
    def my_patch(self, res, method, obj):
        """setup and tear down a patch for some method on obj"""
        patcher = patch.object(obj, method, return_value=res)
        self._service_patcher(patcher)

    def _service_patcher(self, patcher):
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_single_unvested(self):
        grants = [src.grants.grant.Grant(grant_date= TODAY,
                                         total_shares=100)]
        self.my_patch(grants, 'read', src.grants.etrade)
        rsu = src.rsu.RestrictedStock(init_price=1e3, filename='foo')
        self.assertEqual(
            len(rsu.events()), 16
        )
        self.assertEqual(
            sum(a for _, a in rsu.events()),
            1e3 * 100 * (1 - rsu.tax_rate)
        )
