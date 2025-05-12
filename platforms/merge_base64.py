# merge_base64.py
parts = ["1.txt", "2.txt", "3.txt", "4.txt"]  # 각 조각 파일 이름
output_file = "qwindows_base64.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for part in parts:
        with open(part, "r", encoding="utf-8") as f:
            out.write(f.read().strip())  # 줄바꿈 제거하고 붙임

print(f"✅ {output_file} 생성 완료 (총 {len(parts)}개 조각)")
