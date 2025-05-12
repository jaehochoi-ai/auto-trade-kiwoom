from datetime import datetime

def log_trade(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("C:/stock/trade_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")

# 테스트 로그 남기기
log_trade("✅ 테스트 로그: 현재 시간은 종가매매 시간이 아닙니다.")
