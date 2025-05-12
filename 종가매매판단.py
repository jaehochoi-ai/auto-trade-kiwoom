
import yfinance as yf
import pandas as pd

def check_buy_signal(stock_code):
    df = yf.download(stock_code, period="7d", interval="1d")
    if len(df) < 2:
        return False, "데이터 부족"

    today = df.iloc[-1]
    yesterday = df.iloc[-2]

    is_bullish = (today["Close"] > today["Open"])
    is_bullish = is_bullish.item() if hasattr(is_bullish, "item") else is_bullish
    body_ratio = (today["Close"] - today["Open"]) / (today["High"] - today["Low"] + 1e-6)
    long_body = (body_ratio > 0.6)
    long_body = long_body.item() if hasattr(long_body, "item") else long_body
    volume_spike = (today["Volume"] > yesterday["Volume"] * 2)
    volume_spike = volume_spike.item() if hasattr(volume_spike, "item") else volume_spike
   
    prev_high = df["High"].iloc[-5:-1].max()
    breakout = today["Close"] >= prev_high
    if bool(is_bullish) and bool(long_body) and bool(volume_spike) and bool(breakout):
        return True, "조건 충족"
    else:
        return False, "조건 미충족"

# 테스트할 종목 리스트
stock_list = {
    "삼성전자": "005930.KQ",
    "하이브": "352820.KQ",
    "포스코DX": "022100.KQ",
    "에코프로": "086520.KQ",
    "씨아이에스": "222080.KQ"
}

# 실행
for name, code in stock_list.items():
    result, message = check_buy_signal(code)
    print(f"{name} ({code}) → {message}")
