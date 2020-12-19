import scrapy
from ..items import ItArticle


class TestSpider(scrapy.Spider):
    name = 'test6'
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
