# 기본 출력
print('헬로 파이썬!')
# 개행
print()
print('a')


# separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='')  # python
print('010', '1234', '5678', sep='-')  # 010-1234-5678
print('python', 'google.com', sep='@')  # python@google.com


# end 옵션
print('Welcome', end='')
print('IT News', end='')
print('Web Site')  # WelcomeIT NewsWeb Site 이렇게 출력된다.


# file 옵션
import sys

print('Learn Python', file=sys.stdout)


# format 사용(d, s, f) - d: 정수, s: 문자열, f:3.1454545
print('%s %s' % ('one', 'two'))  # one two
print('{} {}'.format('one', 'two'))  # one two
print('{1} {0}'.format('one', 'two'))  # two one


# %s
print('%10s' % ('nice'))  #     nice
print('{:>10}'.format('nice'))  #     nice

print('%-10s' % ('nice'))  # nice          (오른쪽에 10개 공백)
print('{:<10}'.format('nice'))  # nice          (오른쪽에 10개 공백)

print('{:_>10}'.format('nice'))  # ____nice
print('{:^10}'.format('nice'))  #      nice     (중앙정렬)

print('%.5s' % 'pythonStudt')  # pytho (절삭 - 5개만 사용한다는 뜻)


# %d
print('%d %d' % (1, 2))  # 1 2
print('{} {}'.format(1, 2))  # 1 2

print('%4d' % 42)  #  42
print('{:4d}'.format(42))  #  42


# %f
print('%1.3f' % 3.1454545134)  # 3.145
print('{:f}'.format(3.1454545))  # 3.145455
