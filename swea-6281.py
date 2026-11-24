# 6281. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 7
N = int(input())
lst = []
for i in range(1, N + 1):
    if N % i == 0:
        lst.append(i)

print(lst)