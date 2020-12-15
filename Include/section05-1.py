# Section05-1
# BeautifulSoup 사용

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h2 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a data-io="link3" href="http://example.com/little" class="brother" id="link3">Title</a>
        </p>
        <p class="story">
            story......
        </p>
    </body>
</html
"""

# 예제1(기초)
# html 인자 집어넣음 requests.get('http://~~'.text)
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup type : ', type(soup))

# 위에서 가져온 내용을 들여쓰기같은거 다 해서 html태그 형식으로 뿌려줌
print('prettify : ', soup.prettify())

# h1 태그에 접근
h1 = soup.html.body.h1  # 순서대로 접근할수 있음 가장 위에 html 그다음 head 그 아래 바로 자식이 title 이런식으로

print('h1 : ', h1)  # <h1>this is h1 area</h1> 태그 전체의 값을 가져옴

# p 태그 접근
p1 = soup.html.body.p  # p태그는 body안에 3개있는데..? 가장 위에있는 p를 가져옴

print('p1 : ', p1)  # 같은 태그가 여러개 있으면 첫번째 자식을 가져옴

# 시블링을 한번만하면 p태그 끝으로 이동하고 거기서 한번 더 해서 다음에 있는 태그인 p태그로 이동한거
# 근데 시블링을 한번만하면 b태그로 가는건데 출력은 하지않음
p2 = p1.next_sibling.next_sibling  # 하위태그도 다 가져옴

# p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling 이렇게 4번 호출하면 3번째 p태그인 story... 부분 출력가능 3번 호출하면 두번째 p호출 후 공백 부분으로 가서 4번 호출을 해야함
print('p2 : ', p2)

# 텍스트 출력1
print('h1 >>', h1.string)  # 태그 하위의 텍스트를 호출하는건 string
# 텍스트 출력 2
print('p >>', p1.string)  # b태그는 무시하고 텍스트만 뽑아옴

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element))  # 문자열을 list로 가져옴 이게 중요
# print(p2.next_element)  # 다음 엘리먼트를 추출 다음 요소는 텍스트를 가져오는거

# 반복 출력 확인
for v in p2.next_element:
    pass
   # print(v)  # 한글자씩 출력

# 예제2 find, find_all
# bs4 초기화
soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
# find_all은 선택자에 만족하는걸 전부 가져옴
# 리스트형태로 위에 a태그 3개 반환 // 저렇게 limit=2하면 순서대로 2개만 가져옴
link1 = soup2.find_all('a', limit=2)
# print(type(link1))

# 리스트 요소
# print('links : ', link1)


link2 = soup2.find_all('a', class_='sister')  # a태그 중에 특정 클래스이름만 가져와라
# string이 Elsie인거,Title인거 가져오기
link3 = soup2.find_all('a', string=["Elsie", "Title"])
link4 = soup2.find_all('a', id='link2')
# 전부 리스트로 가져옴
print(link2)
print(link3)
print(link4)

print("="*80)
print("="*80)
print("="*80)
print("="*80)
print("="*80)
for t in link2:
    print(t.string)

link5 = soup.find("a")  # 가장 먼저 있는거 아니면 문서에서 하나만있는거 가져옴
print(link5)
print(link5.string)  # 문자열
print(link5.text)  # 문자열

print("="*80)
print("="*80)
# 다중 조건
# a태그 중에서 클래스가 브라더, 데이터 아이오가 링크3인거
link6 = soup.find("a", {"class": "brother", "data-io": "link3"})
print(link6)
print(link6.text)
print(link6.string)

print("-"*80)
print("-"*80)
print("-"*80)
print("-"*80)
print("-"*80)
print("-"*80)

# 셀렉트는 전체 셀렉는 하나
# find와의 차이

# css 선택자 : select
# 태그로 접근 : find

# find는 태그로 접근해서 태그안에 속성을 가져옴 (a태그에 접근해서 그 안에 속성들을 가져옴)

# 예제3(select,select_one)
# 태그 + 클래스 + 자식선택자
link7 = soup.select_one('p.title > b')  # p에 타이틀 클래스에서 바로 밑 자식태그인 b를 가져오겠다
print(link7)
print(link7.text)
print(link7.string)

link8 = soup.select_one("a#link1")  # a태그의 id가 link1인거 가져오기
print(link8)
print(link8.text)
print(link8.string)

# a태그에 data-io=link3인거 가져오기 대괄호를 쓰면 어떤 속성값을 가져올수있음
link9 = soup.select_one("a[data-io='link3']")
print(link9)
print(link9.text)
print(link9.string)

# 선택자에 맞는 전체 선택
link10 = soup.select('p.story > a')  # p에 스토리클래스에 하위인 a태그 다 가져옴
print(link10)

print('-'*80)

# print(link10.string) # 이건 리스트로 넘어와서 어떤 태그를 string으로 할 지 몰라서 에러
link11 = soup.select('p.story > a:nth-of-type(2)')  # p에 스토리클래스 안에 a의 두번째요소 가져옴
print(link11)

print('*'*80)
print('*'*80)

link12 = soup.select("p.story")  # story 클래스 두개 가져옴 리스트형태로
print(link12)

print('*'*80)
print('*'*80)
print('*'*80)
print('*'*80)
print('*'*80)
print('*'*80)

for t in link12:
    temp = t.find_all("a")

    if temp:
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else:
        print('-----', t)
        print('-----', t.string)
