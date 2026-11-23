# 6275. 파이썬 프로그래밍 기초 파이썬의 기본 응용
# 자료구조 -리스트, 튜플2
word = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
remove = ['a','e','i','o','u']

print(''.join(list(c for c in word if c not in remove)))