
# ha_condition_search.py
# 하승훈 스타일 조건검색기 + 자동 종가매수 전략 (KOSPI + KOSDAQ)

import FinanceDataReader as fdr
import pandas as pd
import datetime

# 오늘 날짜
today = datetime.datetime.now().strftime('%Y-%m-%d')

# 1. 코스피 + 코스닥 종목 리스트 가져오기
kospi_list = fdr.StockListing('KOSPI')
kosdaq_list = fdr.StockListing('KOSDAQ')
stock_list = pd.concat([kospi_list, kosdaq_list], ignore_index=True)

# 2. 조건에 맞는 종목 리스트
selected_stocks = []

# 최대 100개 종목만 테스트 (속도 이슈 방지)
sample_codes = stock_list['Code'][:100]

for code in sample_codes:
    try:
        df = fdr.DataReader(code, start='2024-01-01')
        df = df.dropna()
        if len(df) < 15:
            continue
        df = df.tail(15)

        # 조건 1: 전고점 돌파 (최근 10일 고점 < 오늘 종가)
        recent_high = df['High'][:-1].tail(10).max()
        today_close = df.iloc[-1]['Close']
        if today_close <= recent_high:
            continue

        # 조건 2: 거래량 급등 (전일 대비 2배 이상)
        vol_today = df.iloc[-1]['Volume']
        vol_yesterday = df.iloc[-2]['Volume']
        if vol_today < vol_yesterday * 2:
            continue

        # 조건 3: 양봉 (종가 > 시가)
        if df.iloc[-1]['Close'] <= df.iloc[-1]['Open']:
            continue

        selected_stocks.append((code, today_close))
    except:
        continue

# 3. 조건 통과한 종목 출력
print("✅ 조건검색 결과 ({}):".format(today))
for stock in selected_stocks:
    print("  - 종목코드:", stock[0], "| 종가:", stock[1])

# 4. 자동매수 로직은 키움 OpenAPI 연동 시 연결 예정
# 예: kiwoom.SendOrder(...) 코드로 연동 가능
