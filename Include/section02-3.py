# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑
# pip install lxml, requests, cssselect
import requests
import lxml.html


def main():

    save_path = []

    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """
    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com")  # 요청을 가져와서 데이터를 담음

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        print(url)
        print(type(urls))
        with open('C:/text2.txt', 'w') as c:  # wb는 바이트로 쓰겠다 (write)
            c.write(str(urls))


def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장 위에 네이버에서 정보를 가져왔기떄문에 문자열로 저장해야함
    # response.content 이건 페이지 소스보기했을때 나오는거
    root = lxml.html.fromstring(response.content)

    # css의 선택자만 넣으면 됨
    # 제일 앞부터 자손으로 타고 들어감
    for a in root.cssselect('.thumb_area .thumb_box .popup_wrap a:nth-child(3).btn_popup'):
        # 링크
        url = a.get('href')  # href 속성을 가져옴 그럼 url에 담기게됨
        urls.append(url)
    return urls


    # 스크래핑 시작
if __name__ == "__main__":
    main()
