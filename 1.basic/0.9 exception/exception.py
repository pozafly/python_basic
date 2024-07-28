# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요

# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시 -> 하지말자

# SyntaxError
# print('Error)
# print('error'))

# NameError
# ㅁ = 10
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
# x = [50, 70, 90]
# print(x[4])

# KeyError
dic = {'name': 'Lee', 'Age': 41}
# print(dic['hobby'])  # 에러
print(dic.get('hobby'))  # None

# 에외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError : 참조값 없을 때
x = [10, 50, 90]
x.remove(50)
print(x)
# x.remove(200)  # 예외

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y)  # 예외
print(x + list(y))


# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러 개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

# name = ['Kim', 'Lee', 'Park']
# try:
#     z = 'Kim'  # 'Cho'
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')
# print('pass!')


# name = ['Kim', 'Lee', 'Park']
# try:
#     z = 'Cho'  # 'Cho'
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except Exception:  # 모든 에러를 다 잡겠다. except만 써도 된다.
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')


# except Exception:  이 부분을 except Exception as e: print(e) 도 가능.

# name = ['Kim', 'Lee', 'Park']
# try:
#     z = 'Cho'  # 'Cho'
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except Exception as e:
#     print(e)  # 'Cho' is not in list
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')
# finally:
#     print('Ok! finally')
# finally는 예외가 발생하든 하지 않든 무조건 실행된다.


try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! Pass!')
    else:
        raise ValueError  # 에러를 발생시킨다.
except ValueError:
    print('Occurred!')
else:
    print('Ok! else!')
