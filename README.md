# market watch

### 코스피와 코스닥을 중심으로 한국 시장 마켓타이밍 보기
참고로 볼만 한 유튜브 영상
- [강환국의 할 수 있다! - 알고투자 674. KOSPI 지수의 PBR - 유용한 타이밍 지표인가!](https://youtu.be/B4ojMjg1ni4)
- [홍춘욱의 경제강의노트 - 홍춘욱의 경제특강, 국내주식은 언제 사야할까?](https://youtu.be/9z3IEWe7ejE)


main.py 에서 `korea` 딕셔너리의 구성은 아래의 코드로 확인할 수 있습니다.
```
from pykrx import stock

for ticker in stock.get_index_ticker_list():
    print(ticker, stock.get_index_ticker_name(ticker))
```
