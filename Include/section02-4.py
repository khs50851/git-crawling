# Section02-4
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑

import requests
from lxml.html import fromstring, tostring


def main():

    save_path = []

    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 세션 사용 처음부터 끝까지 로그인한 상태로
    session = requests.Session()  # 세션정보를 가지고 사이트를 요청하고 수신을 받고, 흐름이 끊기지 않음

    # 스크랩핑 대상 URL
    response = session.get("https://www.naver.com")  # 요청을 가져와서 데이터를 담음

    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력
    for name, url in urls.items():
        print(name, url)

    # print(url)
    # with open('C:/text2.txt', 'w') as c:  # wb는 바이트로 쓰겠다 (write)
    #     c.write(str(urls))


def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장 위에 네이버에서 정보를 가져왔기떄문에 문자열로 저장해야함
    # response.content 이건 페이지 소스보기했을때 나오는거
    root = fromstring(response.content)

    # css의 선택자만 넣으면 됨
    # 제일 앞부터 자손으로 타고 들어감
    # 슬러시두개// 이건 전체문서라는 뜻
    for a in root.xpath('//ul[@class="list_theme"]/li[@class="theme_item"]/a[@class="theme_thumb"]'):
        # a 구조 확인
       # print(type(a))
        # a 문자열 출력
        #c = tostring(a, pretty_print=True)
        # print(type(c))
        name, url = extract_contents(a)
        # 딕셔너리 삽입
        urls[name] = url
    return urls


def extract_contents(dom):
    # 링크 주소
    link = dom.get('href')
    # print(link)
    # 제목 명
    name = dom.xpath('./img')[0].get('alt')  # 리스트로 넘어옴
    # print(name)
    return name, link

    # 스크래핑 시작
if __name__ == "__main__":
    main()
