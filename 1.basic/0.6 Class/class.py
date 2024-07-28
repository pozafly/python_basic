# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네입스페이스는 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재


class Dog:  # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        print(self)  # <__main__.Dog object at 0x102ac2a20>
        self.name = name
        self.age = age


print(Dog)  # <class '__main__.Dog'>

# 인스턴스화
a = Dog('mkky', 2)
b = Dog('baby', 3)
c = Dog('mkky', 2)

print(a)  # <__main__.Dog object at 0x102ac2a20>
print(a == c, id(a), id(c))  # False 4379831056 4379831104
# 들어간 매개변수는 동일하지만, id 값이 다르고 인스턴스화 된 객체는 서로 다르다.


# 네임스페이스
print('dog1', a.__dict__)  # dog1 {'name': 'mkky', 'age': 2}
print('dog2', b.__dict__)  # dog2 {'name': 'baby', 'age': 3}

# 인스턴스 속성 확인
print(f'{a.name} is {a.age} and {b.name} is {b.age}')  # mkky is 2 and baby is 3

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))  # mkky is a firstdog
print(Dog.species)  # firstdog
print(a.species)  # firstdog


# self의 이해
class SelfTest:
    def func1():
        print('Func1 called')

    def func2(self):
        print('here')
        print(id(self))
        print('Func2 called')


f = SelfTest()
print(
    dir(f)
)  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'func1', 'func2']

print(id(f))
# f.func1() # 에러
f.func2()  # Func2 called
# func2는 self가 넘어갔다는 뜻이다.

# print(id(f)) == class 안에 있는 self와 같다.

SelfTest.func1()  # 이러면 호출된다.
# SelfTest.func2()  # 에러
SelfTest.func2(f)  # 이러면 호출된다.


# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0  # 재고

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1
