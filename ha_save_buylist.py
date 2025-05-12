# buy_list.txt 파일로 저장
with open("buy_list.txt", "w") as f:
    for stock in selected_stocks:
        f.write(f"{stock[0]}\t{stock[1]}\n")

print("\n📂 buy_list.txt 파일 생성 완료 (조건 통과 종목 저장)")
