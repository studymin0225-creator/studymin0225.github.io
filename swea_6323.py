# 6323 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 4
n = 10
lst = []

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

lst = [fibo(i) for i in range(1,n+1)]
print(lst)
print()
