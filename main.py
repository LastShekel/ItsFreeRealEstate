import argparse
import sys

from typing import Dict, List
from data_norm import real_estate
from download import get_data
from formating import print_dict
import pandas as pd


def _get_town(pivot: pd.DataFrame,
              column: str,
              saleratio_top: int) -> List[str]:
    return list(pivot.iloc[pivot[column].argsort()[-saleratio_top:]].index)


def get_top_saleamount(data_df: pd.DataFrame,
                       saleratio_top: int = 10) -> Dict[int, List[str]]:
    pivot = data_df.pivot_table(index='town',
                                columns='year',
                                values='saleamount',
                                aggfunc='sum')
    pivot = pivot.fillna(0).astype(float)
    result = {
        int(column): _get_town(pivot, column, saleratio_top)
        for column in pivot.columns}
    return result


def get_top_saleratio_towns(data_df: pd.DataFrame,
                            saleratio_top: int = 10) -> List[str]:
    gb = data_df.groupby(['town']).agg({'salesratio': max})
    return list(gb.iloc[gb['salesratio'].argsort()[-saleratio_top:]].index)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Aggregating data for Connecticut real estate')
    parser.add_argument('--saleratio',
                        metavar='saleratio',
                        help='Number of towns with highest salesratio')
    parser.add_argument('--saleamount',
                        metavar='saleamount',
                        help='Number of towns with '
                             'highest saleamount per year')
    args = parser.parse_args(sys.argv[1:])
    saleratio_top, saleamount_top = int(args.saleratio), int(args.saleamount)
    data_df = pd.DataFrame.from_records(get_data())
    data_df = real_estate(data_df)
    if saleratio_top:
        print('%s towns that have the highest '
              'sales ratio ascending order' % saleratio_top)
        print(get_top_saleratio_towns(data_df, saleratio_top))
    if saleamount_top:
        tops = get_top_saleamount(data_df)
        print('%s towns that have the highest '
              'volume of sales for each year ascending order' % saleratio_top)
        print_dict(tops)


if __name__ == '__main__':
    main()