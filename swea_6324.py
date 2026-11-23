# 6324 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 5
list = [1,2,3,4,3,2,1]

def nOtin():
    lst = []
    for i in list:
        if i not in lst:
            lst.append(i)
    print(lst)
    return

print(list)
nOtin()
print()
