# 6321 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 3
s = 13

def prime(s):
    if s < 2:
        print('소수가 아닙니다')
        return
    for i in range(2,s):
        if s % i == 0:
            print('소수가 아닙니다')
            return
        else:
            print('소수입니다')
            return

prime(s)
