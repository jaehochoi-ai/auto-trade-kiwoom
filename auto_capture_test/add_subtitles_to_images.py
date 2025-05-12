from PIL import Image, ImageDraw, ImageFont
import os

# 경로 설정
input_dir = "frames"
output_dir = "frames_with_subtitles"
subtitle_file = "matched_subtitles.txt"

# 저장 폴더 없으면 생성
os.makedirs(output_dir, exist_ok=True)

# 자막 불러오기
with open(subtitle_file, "r", encoding="utf-8") as f:
    lines = [line.strip().split("\t") for line in f if "\t" in line]

for i, (timestamp, subtitle) in enumerate(lines):
    img_path = os.path.join(input_dir, f"frame_{i:04d}.jpg")
    out_path = os.path.join(output_dir, f"frame_{i:04d}.jpg")

    if not os.path.exists(img_path):
        print(f"이미지 없음: {img_path}")
        continue

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    text = subtitle
    text_w, text_h = draw.textsize(text, font=font)
    x = (img.width - text_w) // 2
    y = img.height - text_h - 20

    draw.rectangle([x - 10, y - 10, x + text_w + 10, y + text_h + 10], fill=(0, 0, 0, 180))
    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    img.save(out_path)

print(f"✅ 완료: {output_dir} 폴더에 자막 이미지 저장됨")
