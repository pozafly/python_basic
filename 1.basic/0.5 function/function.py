# 종류
# 1. 매개 변수가 필요한 함수
# 2. 매개 변수가 필요하지 않은 함수
# 3. 결과 값을 반환하는 함수(return)
# 4. 결과 값을 반환하지 않는 함수


def function1():
	print('호출1')


function1()


def function2(a, b):
	print('호출2', a, b)


function2(10, 20)  # 호출2 10 20


def function3(x, y):
	return x + y


r = function3(10, 30)
print(r)  # 40


def first_func(w):
	print('Hello', w)


first_func('goodBoy')  # Hello goodBoy


# 다중 반환
def func_mul(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	return y1, y2, y3


r1, r2, r3 = func_mul(10)
print(r1, r2, r3)  # 100 200 300


# 튜플 리턴
def func_mul2(x):
	y1 = x * 10
	y2 = x * 20
	y3 = x * 30
	return (y1, y2, y3)


q = func_mul2(20)
print(type(q), q)  # <class 'tuple'> (200, 400, 600)


# 중요
# *args, **kwargs
# *는 튜플 형태, **는 딕셔너리 형태


# *args(언팩킹)
def args_func(*args):  # args는 아무거나 들어가도 된다 -> 가변 인자
	for i, v in enumerate(args):
		print('Result: {}'.format(i), v)
	print('----')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')
"""
Result: 0 Lee
----
Result: 0 Lee
Result: 1 Park
----
Result: 0 Lee
Result: 1 Park
Result: 2 Kim
----
"""


# **kwargs(언패킹)
def kwargs_func(**kwargs):
	for k in kwargs.keys():
		print('{}'.format(k), kwargs[k])
	print('-------')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Cho')
"""
name1 Lee
-------
name1 Lee
name2 Park
-------
name1 Lee
name2 Park
name3 Cho
-------
"""
# 즉, *는 튜플 형태, **는 딕셔너리 형태


# 혼합
def example(args_1, args_2, *args, **kwargs):
	print(args_1, args_2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)
# 10 20 ('Lee', 'Kim', 'Park') {'age1': 20, 'age2': 30, 'age3': 40}


# 중첩 함수
def nested_func(num):
	def func_in_func(num):
		print(num)

	print('In Func')
	func_in_func(num + 100)


nested_func(100)
