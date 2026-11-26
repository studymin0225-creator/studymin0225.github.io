# 6297. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 20
n = list(map(int,input().split(',')))
a = [i for i in n if i % 2 != 0]
print(*a, sep=', ')