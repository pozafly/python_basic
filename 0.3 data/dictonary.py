# 딕셔너리 자료형 (순서 x, 키 중복 x, 수정 0, 삭제 0)

# 선언
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'}
b = {
	0: 'Hello Python',
}
c = {'arr': [1, 2, 3, 4]}
d = {
	'Name': 'Niceman',
	'City': 'Seoul',
	'Age': 35,
	'Grade': 'A',
	'Status': True,
}
e = dict(
	[
		('Name', 'Niceman'),
		('City', 'Seoul'),
		('Age', 35),
		('Grade', 'A'),
		('Status', True),
	]
)
# e와 같이 선언할 수도 있다. 하지만 선호되지는 않음.

f = dict(
	Name='Niceman',
	City='Seoul',
	Age=35,
	Grade='A',
	Status=True,
)
# f와 같이 선언하는게 제일 좋다.

print(type(a), a)  # <class 'dict'> {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'}

# 출력
print(a['name'])  # Kim -> 존재하지 않으면 에러 발생
print(a.get('name'))  # Kim -> 존자하지 않으면 None 처리 NOTE: 따라서 get을 많이 씀.
print(b[0])  # Hello Python


# 추가, 수정
a['address'] = 'seoul'
print(a)  # {'name': 'Kim', 'phone': '01033337777', 'birth': '870514', 'address': 'seoul'}
print(len(a))  # 4

#  지원 함수
# dick_keys, dict_values, dict_items: 반복문(__iter__)에서 사용 가능.
print(a.keys())  # dict_keys(['name', 'phone', 'birth', 'address'])
print(list(a.keys()))  # ['name', 'phone', 'birth', 'address']

print(a.values())  # dict_values(['Kim', '01033337777', '870514', 'seoul'])
print(list(a.values()))  # ['Kim', '01033337777', '870514', 'seoul']

print(
	a.items()
)  # dict_items([('name', 'Kim'), ('phone', '01033337777'), ('birth', '870514'), ('address', 'seoul')])
print(
	list(a.items())
)  # [('name', 'Kim'), ('phone', '01033337777'), ('birth', '870514'), ('address', 'seoul')]


# pop
print(a.pop('address'))  # seoul
print(a)  # {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'}

print(f.popitem())  # ('Status', True)
print(f)  # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 35, 'Grade': 'A'}
print(f.popitem())  # ('Grade', 'A')
print(f)  # {'Name': 'Niceman', 'City': 'Seoul', 'Age': 35}
print(f.popitem())  # ('Age', 35)
print(f)  # {'Name': 'Niceman', 'City': 'Seoul'}


# in 연산자 - key가 있는지 조회할 수 있음.
print('birth' in a)  # True
print('City' in d)  # True

# 수정 & 추가
a['address'] = 'test'
a.update(birth='test')

temp = {'address': 'test'}
a.update(temp)
