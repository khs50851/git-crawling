# Section02-1
# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크래핑

import urllib.request as req

# 파일 URL
img_url = 'data:image/jpeg;base64,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'
html_url = 'http://google.com'
img_url2 = 'https://www.google.com/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.5-s.png'

# 다운받을 경로
save_path1 = 'C:/test1.jpg'
save_path2 = 'C:/index.html'
save_path3 = 'C:/googlelogo.png'
# 예외 처리

# 파일과 헤더를 받는데 어디서 받냐면 request << 여기서 받음
# urlretrieve 함수는 2개를 반환하는데 다운로드 받아올 파일과
# 수신정보를 반환 헤더정보로 수신을하고 전송을 함
# http는 1회성 연결임, 요청을하고 응답을하고 연결이 끊어짐
# 그래서 실행해보면 connection에 close되어있음 마지막에
# 그렇기에 쿠키값을 이용해서 세션을 유지
try:
    file1,header1 = req.urlretrieve(img_url,save_path1) 
    file2,header2 = req.urlretrieve(html_url,save_path2)
    file3,header3 = req.urlretrieve(img_url2,save_path3) 
except Exception as e:
    print("Download failed")
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)
    print(header3)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print('Filename3 {}'.format(file3))
    print()

    # 성공
    print('Download Succeed')