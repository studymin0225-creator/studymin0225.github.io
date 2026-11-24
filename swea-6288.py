# 6288. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플 12
lst = []
for i in range(1, 21):
    if i % 3 != 0 or i % 5 != 0:
        lst.append(i * i)

print(lst)