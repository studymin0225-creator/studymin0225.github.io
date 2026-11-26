# 6293. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 17

from math import pi
r = list(map(int,input().split(',')))
print(', '.join(f'{(2 * i * pi):.2f}' for i in r))