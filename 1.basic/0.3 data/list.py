# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]

# 인덱싱
print(type(d), d)  # <class 'list'> [1000, 10000, 'Ace', 'Base', 'Captain']
print(d[1])  # 10000
print(d[-1])  # Captain
print(e[-1][1])  # Base
print(list(e[-1][1]))  # ['B', 'a', 's', 'e']

# 슬라이싱
print(d[0:3])  # [1000, 10000, 'Ace']
print(d[2:])  # ['Ace', 'Base', 'Captain']
print(d[:])  # [1000, 10000, 'Ace', 'Base', 'Captain']
print(d[::2])  # [1000, 'Ace', 'Captain']
print(d[::-1])  # ['Captain', 'Base', 'Ace', 10000, 1000]


# 리스트 연산
print(c + d)  # [70, 75, 80, 85, 1000, 10000, 'Ace', 'Base', 'Captain']
print(c * 3)  # [70, 75, 80, 85, 70, 75, 80, 85, 70, 75, 80, 85] -> 순서는 유지하고 있음.
print('test' + str(c[0]))  # test70


# 값 비교
print(c == c[:3] + c[3:])  # True

# Identity(id)
print(c == [70, 75, 80, 85])  # True

temp = c
print(temp == c)  # True
print(id(temp), id(c))  # 4372926592 4372926592


# 리스트 수정, 삭제
c[0] = 4
print(c)  # [4, 75, 80, 85]

c[1:2] = ['a', 'b', 'c']
print(c)  # [4, 'a', 'b', 'c', 80, 85]
c[1] = ['a', 'b', 'c']
print(c)  # [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]
# 참고, c[1:2] 에 넣는 것과 c[1]에 넣는 것은 다르다. c[1]은 리스트 자체가 들어갔고, c[1:2]는 리스트가 풀어져 들어간다.

c[1:3] = []
print(c)  # [4, 'c', 80, 85] -> 배열 원소가 삭제된다.

del c[2]
print(c)  # [4, 'c', 85]


# 리스트 함수
a = [5, 2, 3, 1, 4]
# a[5] = 10  # syntax error -> list assignment index out of range
a.append(10)
print(a)  # [5, 2, 3, 1, 4, 10]
a.sort()
print(a)  # [1, 2, 3, 4, 5, 10]
a.reverse()
print(a)  # [10, 5, 4, 3, 2, 1]
# 단, 10억개의 데이터가 있다면 굉장히 오래걸릴 것이다.

print(a.index(3), a[3])  # 3 3
a.insert(2, 7)
print(a)  # [10, 5, 7, 4, 3, 2, 1]
a.reverse()
print(a)  # [1, 2, 3, 4, 7, 5, 10]

# del a[6]
a.remove(10)
print(a)  # [1, 2, 3, 4, 7, 5]
print(a.pop())  # 5
print(a)  # [1, 2, 3, 4, 7]
print(a.count(4))  # 1 -> 1개가 있다.

ex = [8, 9]
a.extend(ex)
print(a)  # [1, 2, 3, 4, 7, 8, 9]
# 하지만 append 하면 [1, 2, 3, 4, 7, [8, 9]] 이렇게 된다.


# 반복문 활용
while a:
	data = a.pop()
print(data)
