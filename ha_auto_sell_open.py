# ha_auto_sell_open.py
from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget
import sys
import datetime
import time

class KiwoomAPI(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.OnEventConnect.connect(self.login_slot)
        self.dynamicCall("CommConnect()")
        print("🔑 로그인 요청 중...")

    def login_slot(self, err_code):
        if err_code == 0:
            print("✅ 로그인 성공!")
            self.sell_stocks()
        else:
            print("❌ 로그인 실패:", err_code)
            QApplication.instance().quit()

    def sell_stocks(self):
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute <= 5:
            try:
                with open("buy_list.txt", "r") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print("❌ buy_list.txt 파일이 없습니다.")
                QApplication.instance().quit()
                return

            if not lines:
                print("⚠️ 매도할 종목이 없습니다.")
                QApplication.instance().quit()
                return

            account_number = "81027840"  # 👉 너의 실제 계좌번호
            screen_no = "0101"

            for line in lines:
                parts = line.strip().split("\t")
                if len(parts) != 2:
                    continue
                code = parts[0]
                qty = int(parts[1])
                print(f"📤 매도 주문 전송 → 종목코드: {code}, 수량: {qty}")
                self.dynamicCall(
                    "SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                    [
                        "자동매도", screen_no, account_number,
                        2, code, qty, 0, "03", ""  # 2: 신규매도, 03: 시장가
                    ]
                )
            print("🚀 모든 매도 주문 전송 완료!")
        else:
            print("⏱ 현재 시간은 종가매매 시간이 아닙니다.")
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = KiwoomAPI()
    app.exec_()
