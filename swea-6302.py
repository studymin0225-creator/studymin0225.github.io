# 6302. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 25
lst = [12, 24, 35, 70, 88, 120, 155]
ans = [i for i in lst if lst.index(i) != 0 and lst.index(i) != 4 and lst.index(i) != 5]
print(ans)