# for in <collection>
# <Loop body>

for v1 in range(10):  # 0 ~ 9
	print(v1)

for v2 in range(1, 11):  # 1 ~ 10
	print(v2)

for v3 in range(1, 11, 2):  # 1 ~ 10 2칸씩 건너뛰어라
	print(v3)


# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for n in names:
	print('You are: ', n)

lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
	print('Current Number: ', n)

word = 'Beautiful'
for s in word:
	print('word: ', s)

# dic
my_info = {
	'name': 'lee',
	'age': 33,
	'city': 'seoul',
}
for k in my_info:
	print('key: ', my_info[k])

for v in my_info.values():
	print('value: ', v)

for i in my_info.items():
	print('item: ', i)


name = 'FineAppLE'
for n in name:
	if n.isupper():
		print(n)
	else:
		print(n.upper())


# break
number = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for n in number:
	if n == 34:
		print('Found 34')
		break
	print('Current number: ', n)


# continue
lt = ['1', 2, 5, True, 4.3, complex(4)]
for v in lt:
	if type(v) is bool:
		continue
	print('current type: ', v, type(v))  # <class 'int'>


# for - else
number = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in number:
	if num == 49:
		print('Found : 24')
		break
else:
	print('Not Found : 24')
# 즉, else는 반복문 전부를 돌고, 마지막에 실행된다. 단, break 문을 만나면 실행하지 않음.


# 구구단
for i in range(2, 10):
	for j in range(1, 10):
		print(f'{i} X {j} = {i * j}')


# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))  # Reversed <reversed object at 0x102638af0>
print('List', list(reversed(name2)))  # List ['n', 'a', 'm', 'e', 'c', 'A']
