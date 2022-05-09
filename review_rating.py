from time import sleep
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 대략 하나당 소요시간 15초, booksummaries.txt 약 16000권의 책, --> 대략 66시간 소요 예정(괜찮을까요?)


# 책 제목 입력(뒤에 book이 붙은 이유는 책이 아닌 것들이 검색되는 것 방지)
book_name = 'the scarlet letter book'

# 검색 주소
url = 'https://www.amazon.com/s?k=' + book_name


s = HTMLSession()
r = s.get(url)

# html.render 해줌으로써 연결(?) (왠지는 모르겠으나 이거 없으면 실행이 안됨)
r.html.render(sleep=1)

# div data-asin 찾기
products = r.html.find('div[data-asin]')

# 그 중에서 가장 첫 번째 product의 data-asin 속성값 모두 가져오기
asin = products[1].attrs['data-asin']

# 상세 페이지 주소
url = 'https://www.amazon.com/dp/' + asin

"""
http://localhost:8050/render.html ==> docker 활용
설치방법 : https://www.youtube.com/watch?v=8q2K41QC2nQ 및  https://www.lainyzine.com/ko/article/a-complete-guide-to-how-to-install-docker-desktop-on-windows-10/   
뒤의 블로그 내용을 전부 끝낸 후에 유튜브를 보는 것을 추천

"""
r = requests.get('http://localhost:8050/render.html', params={'url' : url, 'wait' : 2})

soup = BeautifulSoup(r.text, 'html.parser')

grade = soup.find('span', {'data-hook' : 'rating-out-of-text'}).text

# 4.6 out of 5 에서 4.6만 출력
print(grade[0:3])
