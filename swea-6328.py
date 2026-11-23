# 6328 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 9
s1 = 'one'
s2 = 'three'

def Longword(w1,w2):
    if len(w1) < len(w2):
        print(w2)
    else:
        print(w1)


Longword(s1,s2)
