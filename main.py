from datetime import date
from pykrx import stock
from scraper.scraper import get_index_data
from scraper.visualizer import visualize


def main():
    # kospi_start = stock.get_index_listing_date('KOSPI').loc['코스피']['발표시점'].replace('.', '')
    # kosdaq_start = stock.get_index_listing_date('KOSDAQ').loc['코스닥']['발표시점'].replace('.', '')
#     kospi_start = '20080101'
#     kosdaq_start = '20080101'
    end = date.today().strftime('%Y%m%d')

    korea = {'KOSPI': '1001', 'KOSDAQ': '2001', '은행': '1022', '통신업': '1020'}

    benchmark = '종가'
    overlaps = ['PBR', '배당수익률']

#     data = {'KOSPI': get_index_data(kospi_start, end, korea['KOSPI']), 
#             'KOSDAQ': get_index_data(kosdaq_start, end, korea['KOSDAQ'])
#             }
    
    start = '20200101'
    data = {key: get_index_data(start, end, korea[key]) for key, value in korea.items()}

    visualize(data=data, benchmark=benchmark, overlaps=overlaps)

if __name__ == '__main__':
    main()
