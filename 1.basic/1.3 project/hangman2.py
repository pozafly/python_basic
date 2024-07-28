import time
import csv
import random

# 처음 인사
name = input('이름을 입력해주세요 : ')

print('안녕하세요, ' + name, 'hangman 게임을 즐겨주세요!')
print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# csv 단어 리스트
words = []
# 문제 csv 파일 로드
with open('./1.2file/resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)
q = random.choice(words)


# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 while
# 찬스 카운트가 남아있을 경우
while turns > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print('_', end=' ')
            failed += 1
    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        print('축하합니다! 추측 문자를 맞추었습니다!')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input('문자를 추측해주세요 : ')

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1
        print('틀렸습니다 🥲')
        print('기회는 ', turns, '번 남았습니다!')

        if turns == 0:
            # 실패 메시지
            print('hangman 게임에 실패했습니다. Bye!')
