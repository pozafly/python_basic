# 숫자형 연산자
"""
+, -, *, /
// : 몫
% : 나머지
abs(x) : 절대 값
pow(x, y) : 제곱
** : 제곱

"""


# 형변환 실습
a = 3.0  # float
b = 6  # int
c = 0.7
d = 12.7
print(type(a), type(b))  # <class 'float'> <class 'int'>

print(a + b)  # 9.0
print(int(True))  # 1
print(float(False))  # 0.0
print(complex(3))  # (3+0j)
print(complex("3"))  # (3+0j) 문자형 -> 숫자형

# 수치 연산 함수
print(abs(-7))  # 7
x, y = divmod(100, 8)  # 100을 8로 나누어진 12, 4
print(x, y)  # (12, 4)


# 외부 모듈
import math

print(math.pi)  # 3.141592653589793
print(math.ceil(5.1))  # 6 올림
