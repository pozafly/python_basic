# 읽기 모드: r, 쓰기 모드: w, 추가 모드: a, 테스트 모드: t, 바이너리 모드 b

# 읽기
import pickle

# r(read), t(text) t가 default 값이기 때문에 r로 해도 된다
# UTF-8이 기본 값임
f = open('./1.2file/resource/it_news.txt', 'r', encoding='UTF-8')

# 속성확인
# print(dir(f))

# 인코딩 확인
print(f.encoding)  # UTF-8
print(f.name)  # ./1.2file/resource/it_news.txt
print(f.mode)  # r

cts = f.read()
print(cts)  #  내용이 출력된다

# 반드시 닫기
f.close()
print()


# 보통 open으로 사용하지는 않는다. `with` 문을 쓴다.
with open('./1.2file/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))  # <str_iterator object at 0x100263070>
    # print(list(c))

# with 문은 알아서 close 해준다. -> 하지만, indent 안에서 반드시 작업해야 함.


# read() : 전체 읽기, read(10) : 10Byte
with open('./1.2file/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)  # Right now gamers can
    c = f.read(20)
    print(c)  #  pay just $1 for acc
    # 이건 커서가 있다는 뜻이다. read 할 때마다 커서가 내부적으로 동작한다.
    f.seek(0, 0)
    c = f.read(20)
    print(c)  # Right now gamers can


# 한 줄 읽기
with open('./1.2file/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.readline()
    print(c)  # Right now gamers can pay just $1 for access to hundreds of titles across PC


# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./1.2file/resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    # ['Right now gamers can \n', 'and Xbox via Microsoft \n', 'ac to \n', ...]
    print()
    for c in cts:
        print(c, end='')


# 파일 쓰기(write)
with open('./1.2file/resource/contents1.txt', 'w') as f:
    f.write('I love python\n')  # 써짐
with open('./1.2file/resource/contents1.txt', 'at') as f:
    f.write('I love python2\n')  # 덮어쓰지 않고, 추가함. at가 append text 이기 때문임.

# writelines: 리스트 -> 파일
with open('./1.2file/resource/contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# write
with open('./1.2file/resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)  # 쓰기. 근데 자주 쓰지는 않음.
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
