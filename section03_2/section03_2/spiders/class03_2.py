import scrapy
import logging  # 외부 로거 가져옴

logger = logging.getLogger('Mylogger')

# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider


class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com',
                       'naver.com', 'daum.net']  # 여기 적혀있는 도메인만 허용함

    # 멀티 도메인 실행방법1
    start_urls = ['http://blog.scrapinghub.com/',
                  'https://naver.com', 'https://daum.net']  # 여기 적혀있는 사이트 다 방문

    # 셋팅즈파일을 동적으로 이게 오버라이딩 되기때문에 이게 먼저 작동됨
    custom_settings = {
        'DOWNLOAD_DELAY': 1
        # 'COOKIES_ENABLED': True
    }

    # 실행방법2
    # def start_requests(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse1)
    #     yield scrapy.Request('https://naver.com')
    #     yield scrapy.Request('https://daum.net')

    # # 실행방법2 request 각각지정
    # def parse1(self, response):
    #     pass

    def parse(self, response):
        #  logger.info('Response URL*** : %s' % response.url)
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response Status*** : %s' % response.status)

        if response.url.find('scrapinghub'):
            yield{
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        if response.url.find('naver'):
            yield{
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield{
                'sitemap': response.url,
                'contents': response.text[:100]
            }
