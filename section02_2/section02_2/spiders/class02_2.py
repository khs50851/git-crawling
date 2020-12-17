import scrapy


class Class022Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Requset
        """
        for url in response.css('div.post-item > div > a::attr("href")').getall():  # img src나 id href 가져올땐 속성(attr)을 씀
            # url 바로 사용 보다 urljoin 사용
            # print(url)
            # 여기서 request안에 url을 넣으면 저 url로 다시 요청을 하는거임
            # 왜냐면 기본 https:~~ 이런거 생략되고 그냥 알맹이만 있을수도 있어서임
            # 이렇게 url조인 하면 start_urls에 http://blog.scrapinghub.com/ 이 부분을 url 앞에다 붙여줌 만약 붙어있으면 그대로 가고 안붙어있으면 붙여줌
            # 그럼 이제 이 요청된 데이터를 처리할 함수가 뭐냐고 묻는데 그걸 self.parse_title을 씀
            yield scrapy.Request(response.urljoin(url), self.parse_title)

    def parse_title(self, response):  # 저 url 10개에 대한 response가 또 넘어오는거임
        """
        상세 페이지 -> 타이틀 추출
        :param : response
        :return : Text
        """
        contents = response.css(
            'div.section.post-body > span > p::text').extract()[:10]  # getall() # 마지막[:10] 은 저 p태그를 리스트로 가져오니까 10개까지만 가져오게 하는거
        print(contents)
        yield {'contents': "".join(contents)}
