import scrapy
from ..items import ItArticle

# Scrapy Feed Export 실습
# 출력 형식
# JSON, JSON Lines
# CSV
# XML, Pickle, Marshal

# 저장 위치
# Local File System - 내 컴퓨터
# FTP -(Server) 회사에서 한걸 다른 서버로 전송할 수 있음
# S3 - (AWS) Amazon
# 기본 콘솔

# 방법 2가지
# 1. 커맨드 이용
# -o 파일명, -t 파일형식
# 옵션 설정 예) --set=FEED_EXPORT_INDENT = 2

# 2. Settings.py 이용
# 자동으로 저장(파일명, 형식, 위치)


class TestSpider(scrapy.Spider):
    name = 'test7'
    allowed_domains = ['itnews.com.au']
    start_urls = ['https://www.itnews.com.au/']

    def parse(self, response):
        """
        :param : response
        :return : request
        """

        for url in response.css('div.row.collapse div.article-list-top > a::attr("href")').getall():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """
        :param : response
        :return : Items
        """
        item = ItArticle()
        item['title'] = response.xpath(
            '//h1[@id="article-headline"]/text()').get()
        item['img_url'] = response.xpath(
            '//img[@id="ContentPlaceHolder1_ucArticle_imgImage"]/@src').get()
        item['contents'] = ''.join(response.xpath(
            '//div[@id="article-body"]/p/text()').getall())

        print(type(item))  # item은 dict로 형변환 가능 dict(item) 이럻게
        print(dir(dict(item)))
        yield item
