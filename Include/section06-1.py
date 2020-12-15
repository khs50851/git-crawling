# Selenium
# 다운로드 링크 https://sites.google.com/a/chromium.org/chromedriver/downloads

# 셀레니움을 쓰는 이유는 어떤 후에, 후처리 되는 렌더링을 통해 정보를 표시해주는 그런 서버쪽 프로그래밍이 되어있는 사이트들은
# 리퀘스트 모듈이나, urlretrieve로 조회했을때 데이터가 없음..
# 그리고 실질적인 브라우저로 접근해야하는 곳도 있기때문

# selenium 임포트
from selenium import webdriver

# webdriver 설정(크롬,firefox, ie 등)
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)  # 컴터마다 사양이 다르므로 약간 기다려줌 (5초까지 기다려주는거임)

# 속성 확인
# print(dir(browser))

# 브라우저 사이즈

browser.set_window_size(1920, 1280)  # maximize_window(),minimize_window()

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용
# print('Page Contents : {}'.format(browser.page_source))

print()
print()

# 세션 값 출력
print('Session ID : {}'.format(browser.session_id))

# 타이틀 출력
print('Title : {}'.format(browser.title))  # 웹페이지의 타이틀 출력

# 현재 url 출력
print('Url : {}'.format(browser.current_url))

# 쿠키정보
print('Cookies : {}'.format(browser.get_cookies()))

# 검색창 input 선택
element = browser.find_element_by_css_selector(
    'div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('남자옷코디')  # 이렇게 지정해서 실제로 키를 입력하는것처럼 함

# 검색(Form Submit) 엔터를 쳐주는 역함
element.submit()

# 스크린 샷 저장1
browser.save_screenshot("C:/website_ch1.jpg")

# 스크린 샷 저장1
browser.get_screenshot_as_file("C:/website_ch2.jpg")

# 브라우저 종료
browser.quit()
