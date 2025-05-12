
# ha_condition_search_and_buylist.py
# 조건검색 → 종가매수 종목 저장 자동화

import FinanceDataReader as fdr
import pandas as pd
import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')

# KOSPI + KOSDAQ 리스트 가져오기
kospi = fdr.StockListing('KOSPI')
kosdaq = fdr.StockListing('KOSDAQ')
stock_list = pd.concat([kospi, kosdaq], ignore_index=True)

selected_stocks = []
sample_codes = stock_list['Code'][:100]

for code in sample_codes:
    try:
        df = fdr.DataReader(code, start='2024-01-01')
        df = df.dropna()
        if len(df) < 15:
            continue
        df = df.tail(15)

        recent_high = df['High'][:-1].tail(10).max()
        today_close = df.iloc[-1]['Close']
        if today_close <= recent_high:
            continue

        vol_today = df.iloc[-1]['Volume']
        vol_yesterday = df.iloc[-2]['Volume']
        if vol_today < vol_yesterday * 2:
            continue

        if df.iloc[-1]['Close'] <= df.iloc[-1]['Open']:
            continue

        selected_stocks.append((code, today_close))
    except:
        continue

# 결과 출력
print("✅ 조건검색 결과 ({}):".format(today))
if selected_stocks:
    for stock in selected_stocks:
        print("  - 종목코드:", stock[0], "| 종가:", stock[1])
else:
    print("  - 조건에 맞는 종목이 없습니다.")

# buy_list.txt 파일로 저장
with open("buy_list.txt", "w") as f:
    for stock in selected_stocks:
        f.write(f"{stock[0]}	{stock[1]}
")

print("\n📂 buy_list.txt 파일 생성 완료 (조건 통과 종목 저장)")
