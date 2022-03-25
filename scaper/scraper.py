from datetime import date, timedelta
from pykrx import stock


def get_index_data(start=None, end=None, market=None):
    if not start:
        start = (date.today() - timedelta(days=365)).strftime('%Y%m%d')
    if not end:
        end = date.today().strftime('%Y%m%d')
    if not market:
        market = '1001'

    data = stock.get_index_fundamental(start, end, market)
    data.drop(data[data['PBR']<=0].index, inplace=True)
    return data
