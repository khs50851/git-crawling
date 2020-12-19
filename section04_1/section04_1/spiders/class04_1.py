import scrapy

# Scrapy 환경설정
# 중요

# 실행 방법
# 1. 커맨드 라인 실행 -> scrapy crawl 크롤러명 -s name=value 형태로 씀
# 2. spider 실행시 직접 지정 클래스 안에 custom_settings = {'키' : '값'} 이런 형식으로
# 3. Settings.py에 지정 -> 추천
# 4. 서브 명령어 사용
# 5. 글로벌 설정 : import scrapy.settings.default_settings


class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    def parse(self, response):

        for i, url in enumerate(response.css('div.post-archive div.post-summary-content > a::attr("href")').getall(), 1):
            yield dict(num=i, headline=url)
