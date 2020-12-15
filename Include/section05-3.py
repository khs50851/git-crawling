# Section05-3
# BeautifulSoup

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Login 정보(개발자 도구)
login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': '',
    'password': ''
}

# Headers 정보
headers = {
    "User-Agent": UserAgent().chrome,
    'Referer': 'https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F'
}

with req.session() as s:
    # Requset(로그인 시도)
    res = s.post("https://auth.danawa.com/login", login_info,
                 headers=headers)  # 제너럴의 request URL

    # 로그인 시도 실패 시 예외
    if res.status_code != 200:
        # 여기까진 로그인 실패하든 안하든 똑같이 데이터가 내려오기때문에 로그인 했는지 알 수 없음
        raise Exception("Login failed!")

    # 본문 수신 데이터 확인
    # print(res.content.decode('UTF-8'))

    # 로그인 성공 후 세션 정보를 가지고 페이지 이동
    res = s.get('https://buyer.danawa.com/order/Order/orderList',
                headers=headers)

    # Euc-kr(한글이 깨질경우)
    # res.encoding = 'uec-kr'

    # 페이지 이동 후 수신데이터 확인
    # print(res.content.decode('utf-8'))

    # bs4 초기화
    soup = BeautifulSoup(res.text, 'html.parser')

    # 로그인 성공 체크
    check_name = soup.find('p', class_='user')
    # print(check_name.text)
    if check_name is None:
        raise Exception('Login failed. Wrong Password.')

    # 선택자 사용
    info_list = soup.select(
        "div.my_info > div.sub_info > ul.info_list > li")
    print(info_list)

    # 제목
    print()
    print("***** My Info *****")

    for v in info_list:
        # 속성 메소드 확인
        # print(dir(v))
        proc, val = v.find('span').string.strip(), v.find(
            'strong').string.strip()  # 굳이 a태그 거쳐서 들어가지 않고 걍 바로 strong으로 접근해도 됨
        print('{} : {}'.format(proc, val))
