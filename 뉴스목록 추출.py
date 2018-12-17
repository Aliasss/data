from bs4 import BeautifulSoup
import urllib.request as req

# html 가져오기
url = "https://news.naver.com/"
openurl = req.urlopen(url)

# beautifulsoup로 html 분석
soup = BeautifulSoup(openurl, "html.parser")

# 데이터 추출
a_list = soup.select("div.com_list > div a > strong")
for a in a_list:
    name = a.string
    print('-', name)