# 기본 선언
n = 700

# 출력
print(n)  # 700
print(type(n))  # <class 'int'> -> 자료형

# 동시 선언
x = y = z = 700
print(x, y, z)  # 700 700 700

# 재할당
var = 75
var = "Change Value"
print(var)  # Change Value
print(type(var))  # <class 'str'>

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777
print(n, type(n))  # 777 <class 'int'>

m = n
# m -> 777 <- m
print(m, n)

m = 400  # 재할당 함.
print(m, n)  # 400 777, 기존 n은 변경되지 않았음.


# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 600
print(id(m))  # 4370777712
print(id(n))  # 4370781104
print(id(m) == id(n))  # False
# 즉, id는 고유 값이다.


# 같은 오브젝트 참조
m = 800
n = 800
print(id(m))  # 4313319024
print(id(n))  # 4313319024
print(id(m) == id(n))  # True
# 왜? 파이썬 입장에서 800을 여러 번 할당해서 쓰는 것은 비효율 적이기 때문에
# 효율성을 내부적으로 800을 같은 id에 할당해 사용하는 것임.


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates -> Variable

# 허용하는 변수 선업 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 허용하지 않는 변수
# 1AGE = 7 -> 에러

# 예약어
# for = 3 -> 에러
# class
# as
# if
