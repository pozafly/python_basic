# 리스트와 비교가 중요
# 튜플 자료형(순서0, 중복0, 수정x, 삭제x)
# 불변 -> 중요한 사람의 정보 등 변경되면 안되는 정보.

# 선언
a = ()
b = (1,)  # == (1)
print(type(a), type(b))  # () -> <class 'tuple'> (1) -> <class 'tuple'>
d = (100, 1000, 'Ace', 'Base', 'Captain')

# 인덱싱
print(d[1])  # 1000
print(d[0] + d[1])  # 1100
print(d[-1])  # Captain

# 형 변환
print(list(d))  # [100, 1000, 'Ace', 'Base', 'Captain']
print(type(d))  # <class 'tuple'>
print(type(list(d)))  # <class 'list'>
# 하지만, list를 한번 바꿨다 해서 d 전체가 모두 list가 되는 것은 아니다.

# 수정 x
# d[2] = 'Changed' -> 안된다. typeerror 발생

# 튜플 함수
a = (5, 2, 3, 1, 4, 2)
print(a.index(3))  # 2
print(a.count(2))  # 2

# 팩킹 & 언팩킹(Packing and Unpacking)

# 팩킹 -> 하나로 묶는다
t = ('foo', 'bar', 'baz', 'qux')

# 언팩킹1 -> NOTE: 구조분해 할당 느낌인가?
(x1, x2, x3, x4) = t
print(x1, x2, x3, x4)  # foo bar baz qux
x1, x2, x3, x4 = t  # 괄호가 없어도 된다. -> 하지만, 관습상 괄호가 있는 것이 좋다.
print(x1, x2, x3, x4)  # foo bar baz qux


# 팩킹 & 언팩킹
t2 = 1, 2, 3
t3 = (4,)
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(x1, x2, x3, x4, x5, x6)  # 1 2 3 4 5 6
