from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/seob/PycharmProjects/new/chromedriver")
driver.implicitly_wait(3)

#url에 접근
driver.get("https://ssl.yes24.com//MyPageOrderList/MyPageOrderList")
#로그인
driver.find_element_by_id('SMemberID').send_keys('아이디')
driver.find_element_by_id('SMemberPassword').send_keys('비밀번호')
driver.find_element_by_css_selector('#btnLogin > span.bWrap').click()
# 상품목록에 접근, 목록 데이터 추출
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
products = soup.select("span.txt120")
for i in products:
    print(i.string)