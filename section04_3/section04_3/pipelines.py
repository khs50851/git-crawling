# 파이프 라인 실습(2)
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, 메일 전송


from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv
import xlsxwriter


class TestSpiderPipeline:
    def __init__(self):  # 클래스가 생성될때 초기화 메소드
        # 엑셀 처리 선언
        self.workbook = xlsxwriter.Workbook('C:/result_excel.xlsx')
        # csv 처리 선언(a,w a는 어펜드, w는 쓰는거, w는 덮어서 다시씀)
        self.file_opener = open("C:/result_csv.csv", 'w')
        self.csv_writer = csv.DictWriter(self.file_opener, fieldnames=[
                                         'rank_num', 'site_name', 'daily_time_site', 'daily_page_view', 'is_pass'])
        # 워크시트
        self.worksheet = self.workbook.add_worksheet()
        # 삽입 수
        self.rowcount = 1

    def open_spider(self, spider):  # 최초에 한번 실행 (이미 만들어진거임)
        spider.logger.info('TestSpider Pipeline Started.')

    def process_item(self, item, spider):
        # 즉 마지막에 이 item으로 넘어오는게 item클래스에 있는 item이 넘어옴
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            # 엑셀 저장
            self.worksheet.write('A%s' % self.rowcount, item.get('rank_num'))
            self.worksheet.write('B%s' % self.rowcount, item.get('site_name'))
            self.worksheet.write('C%s' % self.rowcount,
                                 item.get('daily_time_site'))
            self.worksheet.write('D%s' % self.rowcount,
                                 item.get('daily_page_view'))
            self.worksheet.write('E%s' % self.rowcount, item.get('is_pass'))
            self.rowcount += 1

            # CSV 저장
            self.csv_writer.writerow(item)
            return item
        else:
            # 이건 조건에 안맞는거 떨구는거
            raise DropItem(
                f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행
    def close_spider(self, spider):
        # 그리고 셋팅즈 가서 파이프라인 설정해야함

        # 엑셀 파일 닫기
        self.workbook.close()
        # CSV 파일 닫기
        self.file_opener.close()
        spider.logger.info('TestSpider Pipline Closed.')
