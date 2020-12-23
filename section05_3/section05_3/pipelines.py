
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import sqlite3
from scrapy.exceptions import DropItem


class NewsSpiderPipeline:
    # 초기화 메소드
    def __init__(self):
        # DB 설정(자동커밋)
        self.conn = sqlite3.connect('C:/database_db.db', isolation_level=None)
        # DB 연결
        self.c = self.conn.cursor()
        pass

    # Item 건수 별 실행

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('NewsSpider Pipeline Started.')
        self.c.execute(
            "create table if not exists news_data(id integer primary key autoincrement, headline text, contents,parent_link text, article_link text,crawled_time text)")

    def process_item(self, item, spider):
        if not item.get('contents') is None:

            # 삽입 시간
            crawled_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 크롤링 시간 필드 추가
            item['crawled_time'] = crawled_time
            # 데이터 -> DB 삽입
            self.c.execute('insert into news_date(headline,contents,parent_link,article_link,crawled_time) values (?,?,?,?,?);)', (item.get('headline'), item.get(
                'contents'), item.get('parent_link'), item.get('article_link'), item.get('crawled_time')))  # tuple(item[k] for k in item.keys())
            # 로그
            spider.logger.info('Item to DB inserted.')

            return item
        else:
            raise DropItem('Dropped Item. Because This Contents is Empty')

    # 마지막 1회 실행

    def close_spider(self, spider):
        spider.logger.info('NewsSpider Pipeline Started.')
        # 커밋
        self.conn.commit()
        # 연결 해제
        self.conn.close()
