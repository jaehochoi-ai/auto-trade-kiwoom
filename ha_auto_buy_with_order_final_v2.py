
# ha_auto_buy_with_order_final.py
# 조건검색된 종목을 buy_list.txt로부터 불러와 키움 OpenAPI를 통해 자동 매수 주문 전송

from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget
import sys

class KiwoomAPI(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.OnEventConnect.connect(self.login_slot)
        self.login()

    def login(self):
        self.dynamicCall("CommConnect()")
        print("🔑 로그인 요청 중...")

    def login_slot(self, err_code):
        if err_code == 0:
            print("✅ 로그인 성공!")
            self.send_orders_from_file()
        else:
            print("❌ 로그인 실패! 코드:", err_code)
            QApplication.instance().quit()

    def send_orders_from_file(self):
        account_number = "81027840"  # ✅ 새 계좌번호 반영됨
        screen_no = "0101"

        try:
            with open("buy_list.txt", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("❌ buy_list.txt 파일이 없습니다.")
            QApplication.instance().quit()
            return

        if not lines:
            print("⚠️ buy_list.txt에 주문할 종목이 없습니다.")
            QApplication.instance().quit()
            return

        for line in lines:
            parts = line.strip().split("\t")
            if len(parts) != 2:
                continue

            code = parts[0]
            qty = int(parts[1])

            print(f"📦 주문 전송 중 → 종목코드: {code}, 수량: {qty}")

            self.dynamicCall(
                "SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                [
                    "자동매수", screen_no, account_number,
                    1, code, qty, 0, "03", ""  # 1: 신규매수, 0: 시장가, 03: 시장가
                ]
            )

        print("🚀 모든 매수 주문 전송 완료!")
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = KiwoomAPI()
    app.exec_()
