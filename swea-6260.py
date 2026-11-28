# 6260. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 - 셋, 딕셔너리 8
word = input()

print(f'UPPER CASE {sum(1 for i in word if i.isupper())}')
print(f'LOWER CASE {sum(1 for i in word if i.islower())}')