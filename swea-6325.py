# 6325 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 6
l = [2,4,6,8,10]

def findlst(i):
    if i not in l:
        print(f'{i} => False')
    else:
        print(f'{i} => True')

print(l)
findlst(5)
findlst(10)
