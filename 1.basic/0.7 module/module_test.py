import sys


# import time

# print(time.time())  # 1721910552.1007218
# -> 이런 녀석들은 어디에 있는걸까? 어느 위치에 있는걸까?

# sys가 이 경로를 알고 있음.
print(
    sys.path
)  # ['/Users/pozafly/Documents/dev/playground/python_basic/0.6 Class', '/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python312.zip', '/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12', '/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload', '/opt/homebrew/lib/python3.12/site-packages']

print(type(sys.path))  # list
sys.path.append('~/Documents/dev/playground/python_basic/0.6 Class')
import module  # 3.141592653589793  0.4367661062436623

# 이렇게 path를 잡아주면 import가 가능해진다.
# 그리고 파일을 불러왔기 때문에 내부 소스가 바로 실행되어짐.

print(module.add(1, 3))  # 4


# import할 때 모두 다 실행되면 안되기 때문에 __name__을 사용할 수 있다.
# import 하는 파일에 가서 아래 내용을 print 대신 넣자.
# if __name__ == '__main__':
#     print('-' * 15)

# 실행 주체가 자기자신 즉, __main__ 일 경우에만 실행되도록.
