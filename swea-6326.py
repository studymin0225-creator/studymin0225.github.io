# 6326 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 7
N = 5

def fac(N):
    if N <= 1:
        return 1
    else:
        return N * fac(N - 1)

print(fac(N))
