# 파이썬 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

str1 = "Python"
bool = True
str2 = "Anaconda"
float_ = 10.0
int_ = 7
list = [str1, str2]  # ['Python', 'Anaconda']
dict = {"name": "Machine Learning", "version": 2.0}
typle = (7, 8, 9)  # 또는 7, 8, 9 괄호 없이도 가능
set = {7, 8, 9}

print(type(str1))  # <class 'str'>
print(type(bool))  # <class 'bool'>
print(type(str2))  # <class 'str'>
print(type(float_))  # <class 'float'>
print(type(int_))  # <class 'int'>
print(type(list))  # <class 'list'>
print(type(dict))  # <class 'dict'>
print(type(typle))  # <class 'tuple'>
print(type(set))  # <class 'set'>
