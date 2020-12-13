# Section04-1
# requests
import requests

# 세션 활성화
# s = requests.Session()
# r = s.get('https://www.naver.com')
# 수신 데이터
# print(r.text)

# 수신 상태 코드
#print('Status Code : {}'.format(r.status_code))

# 확인
# print('OK? : {}'.format(r.ok))  # true false 반환


# 세션 비활성화
# s.close()  # 항상 어떤 리소스를 사용 하면 close로 닫아야함

s = requests.Session()

# 쿠키 return

r1 = s.get('https://httpbin.org/cookies',
           cookies={'name': 'kwon'})  # 이 쿠키를 실어 보냈는데 응답을 받은거
print(r1.text)

# 쿠키 Set
# 서버쪽에 쿠키를 저장할때 쓰는 메소드
r2 = s.get('https://httpbin.org/cookies/set',  # restAPI url상에도 set이라고 명시해 저장할거란걸 알수있음
           cookies={'name': 'kwon2'})
# print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent': 'good-man_1.0.0_win10_ram16_home_chrome'}

# Header 정보 전송
r3 = s.get(url, headers=headers)
# print(r3.text)

# 우리가 만든 코드가 정상적으로 요청
# 클라이언트가 요청하는데로 정보를 페이로드(실어서) 요청할 수 있음

s.close()

# with문 사용 -> 파일, DB, HTTP 등 외부에 요청하는것들은 with를 써야함
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)
