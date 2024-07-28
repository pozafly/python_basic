# csv는 , 또는 공백 등으로 구분되어 있는 record set 파일.
# 집합을 파일로 저장할 때, DB에 있는 정보를 파일로 저장할 때 사용.
# Python에는 csv를 기본적으로 다룰 수 있는 패키지가 존재함.

# MIME TYPE은 text/csv

import csv

# with open('./1.2file/resource/test1.csv', 'r') as f:
#     reader = csv.reader(f)

#     next(reader)  # Name,Code 이런거 같이 header를 스킵한다.

#     # 객체 확인
#     # print(reader)  # <_csv.reader object at 0x104cacb30>
#     # print(type(reader))  # <class '_csv.reader'>
#     # print(dir(reader))  # __iter__

#     for c in reader:
#         print(c)  # ['Afghanistan', 'AF'] -> list 형태로 가져옴.
#         print(' '.join(c))  #  Zimbabwe ZW -> 포매팅


# with open('./1.2file/resource/test2.csv', 'r') as f:
#     reader = csv.reader(f, delimiter='|')  # 구분자(delimiter)가 | 인 파일의 경우.
#     for c in reader:
#         print(c)


with open('./1.2file/resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # for c in reader:
    #     print(c)  # {'Name': 'Afghanistan', 'Code': 'AF'} -> dict 형태로 가져옴
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------')


# 쓰기
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
with open('./1.2file/resource/write1.csv', 'w', encoding='UTF-8') as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

with open('./1.2file/resource/write2.csv', 'w', encoding='UTF-8') as f:
    # 필드명
    fields = ['One', 'Two', 'Three']

    # Dict write
    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})
