import scrapy

# xpath 선택자 도움 사이트
# https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
# www.nextree.co.kr/p6278/

# css 선택자 도움 사이트
# https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors

# 타겟 데이터는 크롬 개발자 도구 사용

# 선택자 연습 팁 : scrapy shell에서 연습(효율성)
# scrapy shell 도메인 <- 이런식으로 실행


class TestSpider(scrapy.Spider):
    # 스파이더 이름(실행 할때 사용)
    name = 'test5'
    # 허용 도메인
    allowed_domains = ['w3schools.com']
    # 시작 url 여러개 집어넣을수있음
    start_urls = ['https://www.w3schools.com/']

    # css 선택자
    # A B : 자손 그 하위에 여러개 태그가 있어도 존재만하면 가져옴
    # A > B : 자식(바로 아래 하위를 가져옴 그래서 순서를 생각해야함)
    # ::text -> 노드 텍스트만 추출(예를 들면 a태그에 있는 텍스트만 추출할때)
    # ::attr(name) -> 노드 속성값 추출 href같은거
    # get(), getall() 사용 숙지
    # get(default='none') 디폴트값 지정

    # 예)
    # response.css('title::text').get() : 타이틀 태그의 텍스트만 추출
    # response.css('div > a::attr(href)').getall() : div 태그의 자식 a 태그의 href 속성 값 전부 추출

    # Xpath 선택자
    # nodename : 이름이 nodename 선택
    # text() : 노드 텍스트만 추출
    # / : 루트(맨처음 위 가장 상위의 부모부터 시작)
    # // : 현재 node부터 문사상의 모든 노드 조회
    # . : 현재 노드
    # .. : 현재 노드의 부모 노드
    # @ 속성 선택자
    # extract(), extract_first() 사용 숙지

    # 예)
    # response.xpath('/div') : 루트 노드부터 모든 div태그 선택
    # response.xpath('//div[@id="id"]/a/text()').get() : div 태그중 id가 id인 자식 a 태그의 텍스트를 추출
    #
    # 중요
    # get() == extract_first()
    # getall() == extract()

    # 혼합 사용 가능
    # response.css('img').xpath('@src').getall() : 이미지태그의 src속성을 전부 가져오라함

    # nav 메뉴 이름 크롤링 실습
    # 쉘 실행 -> 선택자 확인 -> 코딩 -> 데이터 저장(프로그램 테스트)

    def parse(self, response):
        # 둘다 가능
        # response.css('nav#mySidenav > div.w3-bar-block a::text')
        # response.xpath('//nav[@id="mySidenav"]/div[@class="w3-container"]//a/text()').extract() 모든 노드 a 태그 가져오는거니까 a 앞에 // 이렇게 슬래시 두개 들어가야함
        for n, text in enumerate(response.xpath('//nav[@id="mySidenav"]/div[@class="w3-container"]//a/text()').extract(), 1):
            yield {
                'num': n,
                'Learn Title': text
            }
