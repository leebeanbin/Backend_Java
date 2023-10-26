import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# 검색할 키워드와 이미지 다운로드 폴더 지정
search_query = 'Person'
download_folder = '/Users/leejungbin/Desktop/codes/Deepi/pigenv/sample_pics/'
max_images_to_download = 20  # 최대 다운로드 개수를 지정

# 이미지 검색 결과 페이지 URL에 이미지 크기 설정 추가
url = f'https://www.google.com/search?q={search_query}&source=lnms&tbm=isch&tbs=isz:ex,iszw:1920,iszh:1080'

# Google 이미지 검색 페이지에 GET 요청 보내기
response = requests.get(url)

# Beautiful Soup를 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 이미지 URL 추출 및 다운로드
downloaded_images = 0  # 다운로드한 이미지 개수를 추적

# 첫 번째 이미지 태그를 찾아서 스킵
first_img_tag = soup.find('img')
if first_img_tag:
    first_img_url = first_img_tag.get('src')
    if first_img_url:
        downloaded_images += 1

for img_tag in soup.find_all('img'):
    if downloaded_images >= max_images_to_download:
        break  # 이미지 다운로드 개수가 제한에 도달하면 종료
    if img_tag != first_img_tag:  # 첫 번째 이미지 태그가 아닌 경우에만 처리
        img_url = img_tag.get('src')
        if img_url:
            # 상대 경로를 절대 URL로 변환
            abs_img_url = urljoin(url, img_url)
            img_data = requests.get(abs_img_url).content
            # 이미지 파일 저장
            with open(os.path.join(download_folder, f'image_{downloaded_images + 1}.jpg'), 'wb') as img_file:
                img_file.write(img_data)
            downloaded_images += 1  # 다운로드한 이미지 개수 증가

print(f'{downloaded_images} images downloaded.')