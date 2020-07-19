import unittest
from unittest.mock import patch
import datetime
import pandas as pd
import src.rsu


NOW = datetime.datetime.now().date()


class RSUTestCase(unittest.TestCase):
    def my_patch(self, res, method, obj):
        """setup and tear down a patch for some method on obj"""
        patcher = patch.object(obj, method, return_value=res)
        self._service_patcher(patcher)

    def _service_patcher(self, patcher):
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_single_unvested(self):
        df = pd.DataFrame({
            'Plan Type': ['Rest. Stock'],
            'Grant Date': [NOW.isoformat()],
            'Unvested Qty.': [100]
        })
        self.my_patch(df, '_read_etrade', src.rsu.RestrictedStock)
        rsu = src.rsu.RestrictedStock(init_price=1e3)
        self.assertEqual(
            len(rsu.events()), 16
        )
        self.assertEqual(
            sum(a for _, a in rsu.events()),
            1e3 * 100 * (1 - rsu.tax_rate)
        )