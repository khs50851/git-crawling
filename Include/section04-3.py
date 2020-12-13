# Section04-3
# requsets
import requests
# RestAPI : GET, POST, DELETE, PUT : UPDATE, REPLACE(FETCH : UPDATE, MODIFY)
# 중요(이걸 왜 쓰는지?) : URL을 활용해서 자원의 상태 정보를 주고 받는 모든것을 의미
# 예를 들면 /movies 뒤에 이런게 붙으면 영화를 전부 조회를 하는 등
# url 요청만 봐도 어떤 요청을 하는지 알 수 있게됨

# 세션 활성화
s = requests.Session()

# 예제1
r = s.get('https://api.github.com/events')

# 수신 상태 체크
r.raise_for_status()  # 에러가 나면 예외가 발생하고 예외처리하고 끝남

# 출력
# print(r.text)

# 예제2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name', 'Kwon', domain="httpbin.org", path='/cookies')

# 요청  name은 kwon으로 넘어가고 적당한 경로에 쿠키가 저장되어있을거임 도메인도 이 서버 정보가 넘어감
r = s.get('http://httpbin.org/cookies', cookies=jar)
print(r.text)

# 예제3
# 깃허브 사이트가 죽어있을수도 있으니까 5초동안 응답이 올때까지 기다림
r = s.get('https://github.com', timeout=5)

# 출력
# print(r.text)

# 예제4
r = s.post('http://httpbin.org/post',
           data={'id': 'test77', 'pw': '111'}, cookies=jar)
print(r.text)
print(r.headers)

# 예제5
# 요청(POST)
payload1 = {'id': 'test22', 'pw': '222'}
# 튜플형태도 가능 (근데 튜플안에 튜플이어야함) 딕셔너리 형태니까 콤마로 구분해야함
payload2 = (('id', 'test265'), ('pw', '256442'))
r = s.post('http://httpbin.org/post', data=payload2)

# 출력

# print(r.text)

# 예제6(PUT)
r = s.put('http://httpbin.org/put', data=payload1)
print(r.text)

# 예제7(DELETE)
r = s.delete('http://httpbin.org/delete', data={'id': '10'})

# 출력
print(r.text)

r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.ok)
print(r.headers)
print(r.text)
s.close()
