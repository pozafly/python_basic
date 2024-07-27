# sys
import sys

# argv -> 파이썬이 어느 위치에서 실행할지 알려주는 path
print(
    sys.argv
)  # ['/Users/pozafly/Documents/dev/playground/python_basic/1.1 external function/external.py']

# 강제 종료
# sys.exit()

# 파이썬 패키지 위치
# print(sys.path)


# pickle: 객체 파일 쓰기
import pickle

# 쓰기
f = open('test.obj', 'wb')
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

# 읽기
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))  # {1: 'python', 2: 'study', 3: 'basic'} <class 'dict'>
f.close()


# os: 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename
import os

# print(os.environ)  # 운영체제 정보
print(os.environ['USER'])  # pozafly
# 현재 경로
print(os.getcwd())  # /Users/pozafly/Documents/dev/playground/python_basic


# time: 시간 관련 처리
import time

print(time.time())  # 1721993489.5788312
print(
    time.localtime(time.time())
)  # time.struct_time(tm_year=2024, tm_mon=7, tm_mday=26, tm_hour=20, tm_min=31, tm_sec=49, tm_wday=4, tm_yday=208, tm_isdst=0)
print(time.ctime())  # Fri Jul 26 20:32:15 2024
# 포매팅
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))  # 2024-07-26 20:33:08
# 시간 간격 발생
for i in range(5):
    print(i)
    # time.sleep(2)  # 2초를 기다림


# random
import random

print(random.random())  # 0 ~ 1 실수
print(random.randint(1, 45))  # 1 ~ 45 정수
print(random.randrange(1, 45))  # 1 ~ `44` 정수

d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)  # [1, 4, 2, 5, 3] -> 랜덤하게 섞인다

c = random.choice(d)
print(c)  # 3 -> d 배열에서 하나를 선택해준다.


# webbrowser : OS의 웹 브라우저 실행
import webbrowser
# webbrowser.open('http://google.com')  # 기본 브라우저로 설정된 브라우저가 열림
# webbrowser.open_new('http://google.com')  # 새 창으로 열기
