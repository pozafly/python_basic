str1 = "I am Python"
str2 = "Pyton"

print(type(str1))  # <class 'str'>
print(len(str1))  # 11 공백 포함


# 빈 문자열
str1_t1 = ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))  # <class 'str'> 0
print(type(str2_t2), len(str2_t2))  # <class 'str'> 0


# 이스케이프 문자 -> \
print("I'm Boy")
print('I"m Boy')
print('I\'m"b" Boy')
print("a \t b")  # a   b


# Raw String
print(r"I'\\\m Boy")  # I'\\\m Boy


# 멀티라인 입력 -> 역슬래시로 표현 가능
multi_str = """
sadfjawejfe
lfkjeafhuaehfuaweh
fbsdnfvbad
fgjvhkrweajgk
fajerkgjkarewfjwe
nfjweajkfjaekfjbne
"""
print(multi_str)

asdf = "asdfawef" "awefawedfb"  # asdfawefawefawedfb
print(asdf)


# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How"
str_o4 = "Are"
str_o5 = "You"

print(str_o1 * 3)  # pythonpythonpython
print(str_o2 + " " + str_o1)  # Apple python
print("y" in str_o1)  # True -> includes와 같음
print("y" not in str_o1)  # False


# 문자열 형변환
str_i1 = "10"
str_i2 = "10.1"
str_i3 = "15.5"

print(type(int(str_i1)))  # int
print(type(float(str_i2)))  # float
print(type(float(str_i3)))  # float
print(type(str(float(str_i3))))  # str


# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)
print(
    "Capitalize: ", str_o1.capitalize()
)  # Capitalize:  Python -> 첫번째 문자를 대문자로
print("endswith: ", str_o1.endswith("n"))  # endswith:  True -> 마지막 문자가 무엇인지?
print("replace: ", str_o1.replace("thon", "Good"))  # replace:  PyGood
print("sorted: ", sorted(str_o1))  # sorted:  ['h', 'n', 'o', 'p', 't', 'y']
print("split: ", str_o1.split("y"))  # split:  ['p', 'thon']


# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))  # __iter__

for i in im_str:
    print(i)
"""
G
o
o
d
 
B
o
y
!
"""

# 슬라이싱
str_sl = "Nice Python"

print(str_sl[0:3])  # Nic -> 0 부터 3-1 까지 나옴
print(str_sl[5:])  # Python
print(str_sl[: len(str_sl)])  # Nice Python
print(str_sl[1:4:2])  # ie -> 1 부터 4-1 까지 2칸씩 건너뛰어라
print(str_sl[-5:])  # ython -> 뒤자리부터 5칸 뒤에서부터 끝까지
print(str_sl[1:-2])  # ice Pyth
print(str_sl[::2])  # Nc yhn
print(str_sl[::-1])  # nohtyP eciN -> 역방향으로 가져온다


# 아스키 코드
a = "z"
print(ord(a))  # 122
print(chr(122))  # z
