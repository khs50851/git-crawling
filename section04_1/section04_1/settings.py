# Scrapy settings for section04_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 파일 이름과 따라감
BOT_NAME = 'section04_1'

# 스파이더가 어디있는지? 여기엔 여러개의 스파이더를 돌릴 수 있음
SPIDER_MODULES = ['section04_1.spiders']

# 다른 스파이더 이름을 지정해서 쓸수있음
NEWSPIDER_MODULE = 'section04_1.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'section04_1 (+http://www.yourdomain.com)'

# Obey robots.txt rules

# 타겟사이트 Robots.txt 준수 여부 False면 거부가 되어있어도 작동시킴
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)

# 병렬처리 주석 풀면 크롤러 양이 많을경우 32개까지 요청해서 병렬처리 디폴트는 16개
#CONCURRENT_REQUESTS = 32


# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 다운로드 딜레이
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:

# 웹 사이트 도메인 동시 병렬 처리 개수
# 우린 3개 해봤는데 16개까지 사이트를 동시에 처리 가능
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 특정 웹 사이트 ip 주소 병렬 처리 개수
#CONCURRENT_REQUESTS_PER_IP = 16


# Disable cookies (enabled by default)
# 쿠키 활성화 여부 (True) 놓으면 됨 쿠키나 404같은게 뜨면 트루로 바꾸고 해보는거 추천
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)

# 원격으로 텔넷으로 보는거
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

# 기본 request 헤더값
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 미들웨어는 다른 사람이 만든 뭐 네이버의 보안, 다음사이트 이런거 스크래피로 안될때, 엑셀파일을 사용할 수 있게 해주는
# 미들웨어를 pip인스톨로 설치해서 여기 파일을 복사하면 외부의 미들웨어를 사용할 수 있음

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'section04_1.middlewares.Section041SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'section04_1.middlewares.Section041DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# 파이프라인 설정
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'section04_1.pipelines.Section041Pipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html

#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# 캐시 사용 여부
# 캐시를 사용하면 동일하게 여러번 요청 시 서버 사이드에 부하 절감 가능(변동사항 없을 경우)
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

# 캐시는 예를들면 자주 바뀌지 않는 사이트에 내가 일정 기간으로 크롤링을 하려고 규칙을 세우는데
# 한시간에 한번 크롤링을 하려고한다. 근데 한시간 뒤에 바뀐게 없는데 또 크롤링하고 또 바뀐게 없는데 또하면
# 서버에도 부담을 주고 나도 의미없는 행동을 반복하는거기때문에 이렇게 캐시를 설정하면 크롤러를 돌릴때 컴터가
# 캐시를 먼저 뒤지고 있으면 바로 그걸로 출력하고 없으면 새로 방문해서 하는거 그리고 이 캐시가 유지되는 시간은 내가 30초로 설정한거
# HTTPCACHE_ENABLED = True  # 캐시 사용을 트루로 하고
# HTTPCACHE_EXPIRATION_SECS = 30  # 30초마다 초기화하겠다 (유효기간)
# HTTPCACHE_DIR = 'httpcache'  # 캐시 저장 경로
# HTTPCACHE_IGNORE_HTTP_CODES = []  # 응답 거부캐시
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 오류 처리
# 자동 재시도 설정
# 서버측의 오류나 점검시간을 가지면 크롤링이 실패하는게 그럼 다시 시도함
# RETRY_ENABLED = True

# 재시도 횟수 최대값
# RETRY_TIMES = 2  # 두번 해서 안되면 오류나는거

# 재시도 대상 HTTP 코드
# RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # 이 에러코드가 발생하는것만 재시도를함

# 오류 무시 HTTP 상태 코드
# HTTPERROR_ALLOWED_CODES = [404]  # 404일땐 오류지만 멈추지 않고 계속함

# 모든 상태 코드 오류 무시
# HTTPERROR_ALLOWED_CODES = True # 모든 오류 무시 추천안함
