# Section04-2
# Requests
# requests 사용 스크랩핑(2) - JSON
import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청
r = s.get('https://httpbin.org/stream/100',
          stream=True)  # stream=True 이건 직렬화해서 가져옴 텍스트형태의 데이터를 가져올땐 이걸 쓰는게 좋음

# 수신 확인
# print(r.text)
# print(type(r.text))
# Encoding 확인
# 인코딩 None으로 되어있음 파이썬은 기본 인코딩 utf-8임
print('Before Encoding : {}'.format(r.encoding))

if r.encoding is None:
    r.encoding = 'UTF-8'
print

print('After Encoding : {}'.format(r.encoding))


# 가져온 데이터가 하나의 통 라인으로 되어있음 이걸 한줄한줄 반복할거 그리고 혹시나 있을 캐릭터셋의 방지를 위해 디코드 유니코드에 트루값 줌
for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))  # str타입
    # 문자 타입이니 이제 딕셔너리 형태로 바꿔야함

    # JSON(Dict) 변환 후 타입 확인
    b = json.loads(line)  # 생긴건 똑같은데 dict형태로 바꿈
    # print(b)
    # print(type(b))

    # 정보 내용 출력
    for k, v in b.items():
        print("Key : {}, Value : {}".format(k, v))
        if k == 'headers':
            for m, n in v.items():
                print("headers Key : {}, headers Value : {}".format(m, n))
    print()
    print()
s.close()

r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# header 정보
print(r.headers)

# 본문 정보
print(r.text)

# json 변환
print(r.json())  # 단일 레코드일경우 이렇게 json 형태로 호출할수있음

# key 반환
print(r.json().keys())
print(r.json().values())

# 인코딩 반환
print(r.encoding)

# 바이너리 정보
print(r.content)

s.close()
