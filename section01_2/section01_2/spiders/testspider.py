import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['scrapinghub.com']  # 만약 밑에 daum.net쓰면 여기에도 똑같이 써줘야함

    # 옆으로 daum이나 naver 이런식으로 여러개로 리스트에 병렬처리 가능
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):  # 이 파즈의 리스폰스의 그 페이지 갔다온 정보가 넘어옴
        # print('dir', dir(response))
        print('status', response.status)
        # print('text', response.text)
        pass
