# 6286. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 11
N = 10
em_li = []

def fibo(N):
    if N <= 1:
        return N
    else:
        return (fibo(N - 1) + fibo(N - 2))


print(list(fibo(i) for i in range(1, N + 1)))
