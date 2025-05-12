# clean_subtitles.py

frame_dir = "frames"
subtitle_file = "subtitle.txt"
output_file = "subtitle_cleaned.txt"

import os

# 1. 프레임 개수 확인
frame_count = len([f for f in os.listdir(frame_dir) if f.endswith(".jpg") or f.endswith(".png")])

# 2. 자막 불러오기
with open(subtitle_file, "r", encoding="utf-8") as f:
    subtitles = [line.strip() for line in f if line.strip()]

# 3. 불필요한 줄 우선 제거 (공백, 한 글자, 감탄사 등)
ignore_keywords = ["음", "어", "아", "예", "뭐", "그냥", "응", "하하", "허허"]
subtitles = [line for line in subtitles if len(line) > 1 and line not in ignore_keywords]

# 4. 너무 길면 자막 수 줄이기 (프레임 수까지)
if len(subtitles) > frame_count:
    subtitles = subtitles[:frame_count]
elif len(subtitles) < frame_count:
    print(f"⚠️ 자막 수({len(subtitles)})가 프레임 수({frame_count})보다 적습니다. 일부 프레임은 매칭되지 않습니다.")

# 5. 저장
with open(output_file, "w", encoding="utf-8") as f:
    for line in subtitles:
        f.write(line + "\n")

print(f"✅ 자막 정리 완료: {output_file} 생성됨 ({len(subtitles)}줄)")
