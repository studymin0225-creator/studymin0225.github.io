# 6276. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 - 리스트, 튜플3
ans = []

for i in range(2,10):
    lst = []
    for j in range(1,10):
        if j % 3 != 0 and j % 7 != 0 and i % 3 != 0 and i % 7 != 0:
            lst.append(i * j)
    ans.append(lst)

print(ans)