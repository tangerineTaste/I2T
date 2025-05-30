import os
from PIL import Image
import pytesseract

# Tesseract 실행 파일 경로 설정 (Windows라면 필요할 수 있음)
# 예시 (C드라이브 기준):

# 🔧 수정 포인트
IMAGE_DIR = 'images/episode_1'

# 결과 저장용 리스트
results = []

# 이미지 폴더 내 파일 리스트
for filename in sorted(os.listdir(IMAGE_DIR)):
    if filename.endswith(('.jpg', '.png', '.webp')):
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f'🖼️ 처리 중: {filename}')
        
        # 이미지 열기
        img = Image.open(f'\images\episode_1\캡처.PNG')

        # OCR로 텍스트 추출 (한국어 설정)
        text = pytesseract.image_to_string(img, lang='kor')

        # 결과 저장
        results.append({'filename': filename, 'text': text.strip()})

# 결과 출력
for r in results:
    print(f"\n📝 {r['filename']}\n{r['text']}")
