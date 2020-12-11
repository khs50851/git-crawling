# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명

path_list = ["C:/test.jpg","C:/index.html"]

# 다운로드 리소스 url
target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAxOTA5MDJfMjQy%2FMDAxNTY3NDAyMDM4MDYw.os_ZDi7sjh20bTtiCWBgdR2a9pX_srlcb6aBidCwRzgg.STjlvUMLnJ0q3rq5L8nEwH-t9Y4j74eZZAz2PP2o5JIg.PNG%2FIccyyKZ2FtBsKxHRctS8YLqE3VPE.jpg&type=sc960_832","http://google.com"]

for i,url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url) # 이건 다운로드하지 않음 대신 다른 함수에 인자를 넣을 수 있음
        # 수신 내용
        contents = response.read() # 웹에 갖다 오고 읽어서 contents 변수에 담음

        print('-------------------------------------------------------')
        
        # 상태 정보 중간 출력

        print('Header Info-{} : {}'.format(i,response.info())) # urlopen은 자체로 정보를 갖고있어서 info나 getcode를 할 수 있음
        print('HTTP Status Code : {}'.format(response.getcode()))

        print()
        print('-------------------------------------------------------')

        with open(path_list[i],'wb') as c: # wb는 바이트로 쓰겠다 (write)
            c.write(contents)
            
    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ",e.code) # 에러코드 출력
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ",e.reason) # 에러 이유를 알 수 있음

    # 성공
    else:
        print()
        print("Download Succeed.")