import pandas as pd
from decimal import Decimal
import logging


def real_estate(estate_df: pd.DataFrame) -> pd.DataFrame:
    logging.info('Normalising real estate')
    columns = ['town', 'daterecorded', 'saleamount', 'salesratio']

    estate_df = estate_df[columns].dropna()
    estate_df = estate_df[estate_df['town'] != '***Unknown***']

    estate_df['saleamount'] = estate_df['saleamount'].apply(
        lambda x: Decimal(x))
    estate_df['year'] = pd.to_datetime(estate_df['daterecorded']).dt.year
    estate_df = estate_df.astype({
        'year': int,
        'salesratio': float,
    })
    return estate_df
