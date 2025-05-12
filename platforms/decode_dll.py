import base64

# base64 텍스트 파일 읽기
with open("C:/stock/platforms/qwindows_base64.txt", "r", encoding="utf-8") as f:
    data = f.read().replace("\n", "").replace(" ", "")

# base64 → 바이너리 복원
with open("C:/stock/platforms/qwindows.dll", "wb") as dll:
    dll.write(base64.b64decode(data))

print("✅ 복원 완료! qwindows.dll 파일이 생성되었습니다.")
