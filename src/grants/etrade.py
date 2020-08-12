import os
import dateutil.parser
import logging
import typing
import pandas as pd
import src.grants.grant

LOGGER = logging.getLogger()


def _read_xls(filename) -> pd.DataFrame:
    fpath = os.path.join(os.path.curdir, 'data_inputs', filename)
    xl = pd.ExcelFile(fpath)
    return xl.parse('Unvested')


def read(filename) -> typing.Iterator[src.grants.grant.Grant]:
    for name, group in _read_xls(filename).groupby('Plan Type'):
        if name != 'Rest. Stock':
            LOGGER.warning('Unrecognized plan type: %s', name)
            continue
        for _, row in group.iterrows():
            yield src.grants.grant.Grant(grant_date=dateutil.parser.parse(
                row['Grant Date']).date(),
                                         total_shares=row['Unvested Qty.'])
