from pykrx import stock
from scraper.scraper import get_index_data
from scraper.visualizer import visualize


if __name__ == '__main__':
    kospi_start = stock.get_index_listing_date('KOSPI').loc['코스피']['발표시점'].replace('.', '')
    kosdaq_start = stock.get_index_listing_date('KOSDAQ').loc['코스닥']['발표시점'].replace('.', '')
    end = date.today().strftime('%Y%m%d')

    korea = {'KOSPI': '1001', 'KOSDAQ': '2001'}

    benchmark = '종가'
    overlaps = ['PBR', '배당수익률']

    data = {'KOSPI': get_index_data(kospi_start, end, korea['KOSPI']), 
            'KOSDAQ': get_index_data(kosdaq_start, end, korea['KOSDAQ'])
            }

    visualize(data=data, benchmark=benchmark, overlaps=overlaps)