# 집합 (Set)
# 보통 선형대수학 등 공학과 관련된 데이터를 사용.
# 순서 X, 중복 X 추가 O, 삭제 O

# 선언
a = set()

b = set([1, 2, 3, 4])
c = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz'}
f = {42, 'foo', (1, 2, 3), 0.31344}

print(type(a), a)  # <class 'set'> set()
d = set([1, 2, 2, 2, 2, 2])
print(d)  # {1, 2} -> 중복 허용하지 않음
print(2 in d)  # True


# 튜플 변환
t = tuple(b)
print(type(t), t)  # <class 'tuple'> (1, 2, 3, 4)

# 리스트 변환
le = list(c)
print(le)


# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)  # {4, 5, 6} -> 교집합
print(s1.intersection(s2))  # {4, 5, 6} -> 교집합
# 합집합
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9} -> 합집합
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9} -> 합집합
# 차집합
print(s1 - s2)  # {1, 2, 3} -> 차집합
print(s1.difference(s2))  # {1, 2, 3} -> 차집합
# 곱집합
print(s1 ^ s2)  # {1, 2, 3, 7, 8, 9} -> 곱집합
print(s1.symmetric_difference(s2))  # {1, 2, 3, 7, 8, 9} -> 곱집합

# 중복원소 확인
print(s1.isdisjoint(s2))  # False

# 부분 집합 확인
print(s1.issubset(s2))  # False
print(s1.issuperset(s2))  # False


# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print(s1)  # {1, 2, 3, 4, 5}

s1.remove(2)
print(s1)  # {1, 3, 4, 5}

s1.discard(3)
print(s1)  # {1, 4, 5}
# 단, remove로 없는걸 지우면 에러이고, discard로 지우면 에러가 나지 않음.

s1.clear()  # 전체 지움
print(s1)  # set()
