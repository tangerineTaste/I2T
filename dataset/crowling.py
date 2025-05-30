import os
import requests
from bs4 import BeautifulSoup

# 🔧 수정 포인트
WEBTOON_ID = '737628'  # 별이삼샵
EPISODE_NO = '1'
SAVE_DIR = f'images/episode_{EPISODE_NO}'

# 1. 저장 폴더 만들기
os.makedirs(SAVE_DIR, exist_ok=True)

# 2. 웹툰 페이지 요청
url = f'https://comic.naver.com/webtoon/detail?titleId={WEBTOON_ID}&no={EPISODE_NO}'
print(url)
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# 3. 이미지 추출
img_tags = soup.select('div#sectionContWide img')

print(f'✅ 총 {len(img_tags)}장의 이미지 발견')

# 4. 이미지 저장
for idx, img in enumerate(img_tags):
    img_url = img['src']
    ext = img_url.split('.')[-1].split('?')[0]  # jpg, png 등 추출
    file_path = os.path.join(SAVE_DIR, f'cut_{idx+1:03}.{ext}')

    img_data = requests.get(img_url).content
    with open(file_path, 'wb') as f:
        f.write(img_data)

    print(f'📥 저장 완료: {file_path}')
