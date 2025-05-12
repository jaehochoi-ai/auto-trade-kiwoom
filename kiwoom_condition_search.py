from pykiwoom.kiwoom import Kiwoom
import time

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 조건식 리스트 불러오기
conditions = kiwoom.GetConditionNameList()
print("등록된 조건식 목록:")
for idx, name in conditions.items():
    print(f"{idx}: {name}")

# 예시: "눌림목 기초 1" 조건식 번호가 2번이라면
condition_index = 2
condition_name = "눌림목 기초 1"

# 조건검색 실행
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)
print("검색된 종목 코드 목록:", codes)
