# Section06-2
# Selenium 실습

# selenium 임포트
from selenium import webdriver
import time
from selenium.webdriver.common.by import By  # ~~까지 기다릴때
# 드라이버가 로딩될때까지 기다려주는건데 By랑 같이쓰임 보통
from selenium.webdriver.support.ui import WebDriverWait
# 어떤 상태를 예상함, 저 위에 두개랑 같이쓰임
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")  # 크롬 브라우저를 실행하지 않고 내부적으로 함

# webdriver 설정 (Chrome,Firefox 등) - Headless 모드
browser = webdriver.Chrome(
    './webdriver/chrome/chromedriver.exe', options=chrome_options)  # 옵션으로 우리가 만든거 줌

# 크롬 브라우저 내부 내기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1368, 768)  # maximize_window(),minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))
# 좀 더 명확하게 명시적으로 기다리라고함

# 브라우저 객체 넣고 3초간 기달 / 언제까지? 현재 모든 엘리먼트요소가 자기 자리에 위치할때까지(나타날때까지) //

# 내가 선택하려고하는 xpath의 엘리먼트가 브라우저에 나타날때까지 3초까지 기다릴건데 그 전에 나타나면 마우스로 클릭을 해
WebDriverWait(browser, 3).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 만약 3초 동안도 그려지지 않으면 그땐 에러를 뱉어냄


# 더보기 두번쨰
# Implicitly wait
# time.sleep(2)  # 2초 기다림 근데 이건 파이썬 전체엔진이 멈추는거라 좋진 않음
# browser.find_element_by_xpath(
#     '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()


# 원하는 모델 카테고리 클릭

WebDriverWait(browser, 2).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label'))).click()

# 2차 페이지 내용
# print('After Page Contents : {}'.format(browser.page_source))

time.sleep(2)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 소스코드 정리
# print(soup.prettify())

# 메인 상품 리스트 선택
pro_list = soup.select(
    'div.main_prodlist.main_prodlist_list > ul.product_list > li.prod_item.prod_layer')

# 상품 리스트 확인

# print(pro_list)
print(len(pro_list))
count = 0
for v in pro_list:
    # print(v)
    if not v.find('div', class_="ad_header"):  # 광고가 없으면
        # 상품명, 이미지,가격

        if count == len(pro_list)-1:
            break

        else:
            print(v.select('div.prod_main_info > div.prod_info > p.prod_name > a')[
                  0].text.strip())
            print(v.select('a.thumb_link > img')[0]['src'])
            print(v.select('p.price_sect > a')[0].text.strip())
            count += 1
    print()

# 브라우저 종료
browser.close()
