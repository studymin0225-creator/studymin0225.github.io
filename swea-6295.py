# 6295. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 18
col, row = map(int, input().split(','))
print(list([i * j for j in range(row)] for i in range(col)))