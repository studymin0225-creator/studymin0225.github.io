# 6327 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 8
squ = 2,3

def square(s):
    return s * s

for s in squ:
    print(f'square({s}) => {square(s)}')
