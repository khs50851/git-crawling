import scrapy


class Class021Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param : response
        :return : Title Text(제목 텍스트 리턴할거)
        """
        # 2가지(CSS Selector, XPATH)
        # get() 이건 하나만 가져옴<->getall(),extract 이건 전체 <-> extract_first() 이것도 하나만 가져옴

        # css
        # ::text하면 텍스트만 뽑아옴
        # getall하면 리스트로 넘어옴
        # 출력 옵션
        # -o 파일명.확장자 , -t 파일 타입(json,jsonlines,jl,csv,xml,marshal,pickle)
        # for text in response.css('div.post-header > h2 > a::text').getall():
        #     # return type : Request,BaseItem,Dictionary,None 이렇게 4가지중 하나 리턴
        #     yield {'title': text}

        # XPATH
        # 텍스트 뽑아오는건 XPATH에서 함수혀으로함
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall(), 1):
            yield{
                'number': i,
                'text': text
            }
