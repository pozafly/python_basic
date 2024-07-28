"""
참고: Escape 코드

\n : 개행
\t : TAB
\\ : "\" (문자)
\' : "'"
\" : "\" (문자)
\000 : "\0" (널 문자)
"""

# 3가지 Format Practices

x = 50
y = 100
text = 3034893
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, x + y)
print(ex1)  # n = Lee, s = 3034893, sum = 150

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x + y)
print(ex2)  # n = Lee, s = 3034893, sum = 150

# 출력3 f-string
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)  # n = Lee, s = 3034893, sum = 150


# 구분기호
m = 100000000
print(f'm : {m:,}')  # m : 100,000,000


# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽
t = 20
print(f't: {t:10}')
print(f't center: {t:^10}')
print(f't right: {t:>10}')
print(f't left: {t:<10}')

print(f't: {t:-^10}')  # t: ----20----
