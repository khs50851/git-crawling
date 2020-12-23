from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NewsSpider(CrawlSpider):
    name = 'test11'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    # page = \d+ : 연속 , follow=True 이것도 추가
    rules = [
        # LinkExtractor 쓸때는 위에 crawlspipser를 상속 받아야함
        # 만약 d+ 이렇게하면 숫자가 상관 없음(두자리까지 끝까지 감) 플러스 없으면 한자리수만 $이건 정규표현식의 끝을 뜻함

        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'),
             callback='parse_headline'),
    ]

    def parse_headline(self, response):
        # print(response)
        # URL 로깅
        self.logger.info('Response URL : %s' % response.url)

        for m in response.css('ul.list_news2.list_allnews > li > div.cont_thumb'):
            # 헤드라인
            headline = m.css(
                'strong > a::text').extract_first().strip()
            # 본문 20글자
            contents = m.css(
                'div.desc_thumb span.link_txt::text').extract_first().strip()
            yield{
                'headline': headline,
                'contents': contents
            }
