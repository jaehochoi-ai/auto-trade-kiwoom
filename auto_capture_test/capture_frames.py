

import cv2
import os

# 영상 파일 경로
video_path = "video.mp4"
# 저장 폴더
output_dir = "frames"
# 프레임 추출 간격 (초)
interval_sec = 6

# 저장 폴더가 없으면 생성
os.makedirs(output_dir, exist_ok=True)

# 비디오 로드
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
interval_frame = int(fps * interval_sec)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % interval_frame == 0:
        filename = os.path.join(output_dir, f"frame_{saved_count:04}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"{saved_count} frames saved.")
