import os

# 입력 폴더 경로
input_dir = "frames"
# 출력 파일 이름
output_file = "timestamps.txt"
# 간격 (초)
interval_sec = 6

# 이미지 리스트 정렬
images = sorted(os.listdir(input_dir))
with open(output_file, "w", encoding="utf-8") as f:
    for idx, filename in enumerate(images):
        seconds = (idx + 1) * interval_sec
        minutes = seconds // 60
        sec = seconds % 60
        f.write(f"{filename} → {minutes}분 {sec}초\n")
