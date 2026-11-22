# 6312 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 내장함수 5
mul = 1,2,'4',3

def mUlti(a,b,c,d):
    return a,b,c,d

try:
    mUlti(mul)
except TypeError:
    print('에러발생')