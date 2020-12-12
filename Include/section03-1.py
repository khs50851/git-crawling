# Section03-1
# 기본 스크랩핑

import urllib.request
from urllib.parse import urlparse

# 기본 요청1(엔카)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)  # mem에 수신된 정보가 담김
print(mem)
# 여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('header : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))  # status와 같음
# 소스코드를 읽어오는건데 read안에 숫자는 그만큼의 글자수(바이트)를 출력 그리고 decode를 통해 utf-8형식으로 지정할수있음
print('read : {}'.format(mem.read(100).decode('utf-8')))
print('---------------------------')
# 내가 분석하고 싶은 url을 넣으면 됨
# ParseResult(scheme='http', netloc='www.encar.co.kr', path='', params='', query='test=test', fragment='')
# query만 출력도 되고 scheme만도 출력되고 함
print('pase : {}'.format(urlparse('http://www.encar.co.kr?test=test')))

# 기본 요청2(ipify)
API = "http://api.ipify.org"

# GET 방식 파라미터
values = {
    'format': 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)  # id=test 이런 형태로 인코딩함
print('after param : {}'.format(params))

# 요청 URL 생성
URL = API+"?"+params
print("요청 URL = {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이터 디코딩
text = data.decode('utf-8')
print('response : {}'.format(text))
