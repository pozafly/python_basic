# 자주 사용하는 함수
# str(), int(), tuple() 형변황

# 절대 값
print(abs(-3))  # 3

# all : iterable 요소 검사(참, 거짓) -> 하나라도 Falsy한 값이 있으면 False
print(all([1, 2, '']))  # False
print(all([1, 2, 3]))  # True

# any : or
print(any([1, 2, '']))  # True
print(any([1, 2, 0]))  # True

# chr: 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(67))  # C
print(ord('C'))  # 67

# enumerate: 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'def', 'efg']):
    print(i, name)  # 0 abc  1 def  2 efg


# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))  # [-3, -5, 6]
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))  # [-3, -5, 6]


# id: 객체의 주소값(레퍼런스) 반환
print(id(int(5)))  # 4391508456

# len : 요소의 길이 반환
print(len('abasbvd'))  # 7

# max, min : 최대값 최소값
print(max([1, 2, 3]))  # 3
print(max('python study'))  # y
print(min([1, 2, 3]))  # 1
print(min('pythonstudy'))  # d


# map: 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))  # [1, 3, 2, 0, 5, 6]
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))  # [1, 3, 2, 0, 5, 6]


# pow : 제곱
print(pow(2, 10))  # 1024

# range: 반복 가능한 객체(Iterable) 반환
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
print(list(range(0, -15, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]

# round: 반올림
print(round(6.52341, 2))  # 6.52
print(round(5.6))  # 6

# sorted : 반복 가능한 객체(Iterable) 정렬 후 반환
print(sorted([6, 7, 4, 3, 2, 1, 2]))  # [1, 2, 2, 3, 4, 6, 7]
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))  # ['h', 'n', 'o', 'p', 't', 'y']

# sum
print(sum(range(1, 101)))  # 5050

# type : 자료형
print(type(3))  # <class 'int'>
print(type({}))  # <class 'dict'>

# zip : 반복 가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60])))  # [(10, 40), (20, 50), (30, 60)]
print(list(zip([10, 20, 30], [40, 50])))  # [(10, 40), (20, 50)] -> 짝이 맞는 애들만 반환.
