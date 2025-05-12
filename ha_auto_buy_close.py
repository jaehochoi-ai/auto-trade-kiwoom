
# ha_auto_buy_close.py
# 종가매매 자동화: 15:20 ~ 15:29 사이에 buy_list.txt 종목을 시장가 매수

from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget
import sys
import time
import datetime

class KiwoomAPI(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.dynamicCall("CommConnect()")
        self.OnEventConnect.connect(self.login_slot)

    def login_slot(self, err_code):
        if err_code == 0:
            print("✅ 로그인 성공!")
            self.send_orders_from_file()
        else:
            print("❌ 로그인 실패! 코드:", err_code)
            QApplication.instance().quit()

    def send_orders_from_file(self):
        account_number = "81027840"  # 10자리 계좌번호
        screen_no = "0101"

        try:
            with open("buy_list.txt", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("❌ buy_list.txt 파일이 없습니다.")
            QApplication.instance().quit()
            return

        now = datetime.datetime.now().time()
        if not (datetime.time(15, 20) <= now <= datetime.time(15, 30)):
            print("⏰ 현재 시간은 종가매매 시간이 아닙니다.")
            QApplication.instance().quit()
            return

        for line in lines:
            parts = line.strip().split("\t")
            if len(parts) != 2:
                continue

            code = parts[0]
            qty = int(parts[1])
            print(f"📦 종가 매수 주문 → 종목코드: {code}, 수량: {qty}")

            self.dynamicCall(
                "SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                ["종가매수", screen_no, account_number, 1, code, qty, 0, "03", ""]
            )

        print("🚀 종가 매수 주문 전송 완료")
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = KiwoomAPI()
    app.exec_()
