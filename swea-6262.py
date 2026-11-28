# 6262. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 - 셋, 딕셔너리 10
word = input()
dic = {}

for i in word:
    cnt = dic.get(i, 0)
    dic[i] = cnt + 1

for k, v in dic.items():
    print(f'{k},{v}')