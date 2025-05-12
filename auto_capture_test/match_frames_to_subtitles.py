import os

# 자막 파일과 타임스탬프 파일 경로
subtitle_file = "subtitle_cleaned.txt"

timestamp_file = "timestamps.txt"

# 출력 파일
output_file = "matched_subtitles.txt"

# 자막 파일 읽기
with open(subtitle_file, "r", encoding="utf-8") as f:
    subtitles = [line.strip() for line in f if line.strip()]

# 타임스탬프 파일 읽기
with open(timestamp_file, "r", encoding="utf-8") as f:
    timestamps = [line.strip() for line in f if line.strip()]

# 길이 일치 확인
if len(timestamps) != len(subtitles):
    print(f"❌ 매칭 실패: 프레임 수({len(timestamps)}) ≠ 자막 수({len(subtitles)})")
else:
    print(f"✅ 매칭 시작: {len(timestamps)}개 매칭 중...")

    with open(output_file, "w", encoding="utf-8") as f:
        for ts, line in zip(timestamps, subtitles):
            f.write(f"{ts}  {line}\n")

    print(f"🎉 매칭 완료 → 결과 파일: {output_file}")
