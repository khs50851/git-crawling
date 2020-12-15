# Section05-2
# BeautifulSoup 사용 스크래핑(2) - 이미지 다운로드

import os  # 폴더랑 그런것들을 만들거라
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)
                     ]  # 헤더를 이런식으로 추가 리스트형태로 입력받음

# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자 도구)
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

# 검색어
quote = rep.quote_plus('꼬북칩초코츄러스')
# print(quote)
# URL 완성
url = base+quote

# URL 확인
print('Request URL : {}'.format(url))
print()
# requset
res = req.urlopen(url)  # 다운은 받지 않고 소스코드를 확인할 수 있다
# print(res)

# 이미지 저장 경로
savePath = "C:/imagedown/"  # C:\\imagedown

# 폴더 생성 예외 처리(문제 발생 시 프로그램 종료)
try:
    # 기본 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):  # 세이브패스에 디렉토리가 있냐고 물음
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # 에러 내용
    print('folder creation failed.')
    print('folder name : {}'.format(e.filename))  # 폴더 네임은 filename 으로 넘어옴

    # 런타임 에러
    raise RuntimeError("System Exit!")
else:
    # 생성이 되었거나, 존재할 경우
    print('folder is created')

soup = BeautifulSoup(res, "html.parser")

# print(soup.prettify())

# select로 해보자
img_list = soup.select('div.img_area > a.thumb._thumb > img')

# find로 해보자
img_list2 = soup.find_all("a", class_="thumb _thumb")
# print(img_list2)
# print(img_list)

# for v in img_list2:
#     img_t = v.find('img')  # a태그 하위의 img를 가져옴
#     # print(img_t)
#     print(img_t.attrs['data-source'])
#     req.urlretrieve(img.attrs['data-source'], fullFileName)


for i, img in enumerate(img_list, 1):  # 오른쪽에 1은 시작번호
    # 속성 확인
    # print()
    # print()
    # print(i, img['data-source'])  # data-source 키값만 출력
    # 저장 파일명 및 경로
    # 파일 경로는 savePath이고 그 뒤에는 파일명
    fullFileName = os.path.join(savePath, str(i)+'.png')

    # 파일명 출력
    print(fullFileName)

    # 다운로드 요청
    # 첫번째 인자로는 이미지를 다운받을 경로가 들어가야함 두번째는 저장경로
    req.urlretrieve(img['data-source'], fullFileName)
# 다운로드 완료시 출력
print('Succeed!')
