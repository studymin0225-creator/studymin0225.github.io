# 6329 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 10
def countdown(c):
    if c <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        while c >= 1:
            print(c)
            c -= 1

countdown(0)
countdown(10)
