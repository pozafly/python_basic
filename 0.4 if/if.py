# 기본 형식
print(type(True))  # 0이 아닌 수, 'ab', [1,2,3,...], (1,2,...)
print(type(False))  # 0, '', [], (), {}, set()
# NOTE: [], (), {} 이것도 False다.

if True:
	print('Hello Python')
if '':
	print('Hello Python')  # 실행안됌

if False:
	print('Bad')
else:
	print('Good')


# 논리 연산자
a = 75
b = 40
c = 10
print(a > b and b > c)  # True
print(a > b or b > c)  # True
print(not a > b)  # False
print(not False)  # True

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print(5 + 10 > 3 and 7 + 3 == 10)  # True


score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A':
	print('Pass')
else:
	print('Fail')


id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
	print('관리자 입장')


# 다중 조건문
num = 90
if num >= 90:
	print('A')
elif num >= 80:
	print('B')
elif num >= 70:
	print('C')
else:
	print('F')
