# 파이프 라인 실습(1)
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, 메일 전송


from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class TestSpiderPipeline:

    def open_spider(self, spider):  # 최초에 한번 실행 (이미 만들어진거임)
        spider.logger.info('TestSpider Pipeline Started.')

    def process_item(self, item, spider):
        # 즉 마지막에 이 item으로 넘어오는게 item클래스에 있는 item이 넘어옴
        if item.get('site_name') == 'Google.com':
            item['is_pass'] = True
            return item
        else:
            # 이건 조건에 안맞는거 떨구는거
            raise DropItem(
                f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('TestSpider Pipline Closed.')

    # 그리고 셋팅즈 가서 파이프라인 설정해야함
