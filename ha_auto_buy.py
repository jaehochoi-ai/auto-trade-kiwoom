
# ha_auto_buy.py
# buy_list.txt에 있는 종목을 종가에 매수하는 예시 코드 (모의 매매 형태)

import datetime

# 종가매수 시뮬레이션 출력용
print("📈 자동 종가매수 실행 (모의)")

try:
    with open("buy_list.txt", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("❌ buy_list.txt 파일이 존재하지 않습니다.")
    exit()

today = datetime.datetime.now().strftime('%Y-%m-%d')
print(f"🗓️ {today} 기준 매수 예정 종목:")

for line in lines:
    parts = line.strip().split("\t")
    if len(parts) != 2:
        continue
    code, price = parts
    print(f"✅ 종목코드: {code} | 종가: {price}원 → 매수주문 실행")

print("\n💡 참고: 이 코드는 실전 주문이 아닌 모의 출력입니다.")
print("실전 연동 시 키움 OpenAPI로 주문 함수 연결 필요.")
