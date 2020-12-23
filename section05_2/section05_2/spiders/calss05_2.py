from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItems
import scrapy


class NewsSpider(CrawlSpider):
    name = 'test12'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    # page = \d+ : 연속 , follow=True 이것도 추가
    rules = [
        # LinkExtractor 쓸때는 위에 crawlspipser를 상속 받아야함
        # 만약 d+ 이렇게하면 숫자가 상관 없음(두자리까지 끝까지 감) 플러스 없으면 한자리수만 $이건 정규표현식의 끝을 뜻함

        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'),
             callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)

        for url in response.css('ul.list_news2.list_allnews > li > div.cont_thumb'):
            # URL 신문기사
            article_url = url.xpath('strong/a/@href').get().strip()
            # 요청

            # meta는 딕셔너리 형태로 차일드에 우리가 원하는 데이터를 넘길수있음
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url})

    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        self.logger.info('--------------------------------')
        # 메타는 response.meta['parent_url']이런식으로 키값 가져옴
        self.logger.info('Response From Parent URL : %s' %
                         response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('--------------------------------')

        # 헤드라인
        headline = response.css('h3.tit_view::text').extract_first().strip()

        # 본문
        c_list = response.css('div.article_view > p::text').extract()

        contents = ''.join(c_list).strip()

        yield ArticleItems(headline=headline, contents=contents, parent_link=response.meta['parent_url'], article_link=response.url)
