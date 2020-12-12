# Section03-3
# 다음 주식 정보 가져오기
import json
# 사이트에서 내려주는 데이터 타입이 json이기때문에  json 임포트
import urllib.request as req
from fake_useragent import UserAgent

# Fake Header정보 (가상으로 User-angent 생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# Header 정보
headers = {  # request에 유저 에이전트랑 레퍼러만 넣어줄거 referer는 해당 사이트 전에 어디 사이트를 통해 들어온건지
    'User-agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL

url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청

# 리퀘스트 객체 클래스 안에다가 url넣고 헤더스 넣음 인자를 두개받아서 우리가 요청하는것처럼 사이트 requestheader에 요청함
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# 응답 데이터 확인(Json Data)
# print('res : {}'.format(res))

# 응답 데이터 str -> json 변환 및 data 값 출력

rank_json = json.loads(res)['data']  # 키값을 넣으면 됨

# 중간 확인
# print('중간 확인 : ', rank_json, '\n')  # 리스트로 뽑아옴

for elm in rank_json:
   # print(type(elm))  # 리스트 안에 딕셔너리 형태로 저장되어있는거
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(
        elm.get('rank'), elm.get('tradePrice'), elm['name']))
