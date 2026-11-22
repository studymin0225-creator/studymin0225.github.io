# swea 문제 풀이
# 6319 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 1
def ispalindrome(s):
    if s == s[::-1]:
        print(s[::-1])
        print('입력하신 단어는 회문(Palindrome)입니다.')
    else:
        print(s[::-1])
        print('입력하신 단어는 회문(Palindrome)이 아닙니다.')

s = 'eye'
ispalindrome(s)


# 6321 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 3
s = 13

def prime(s):
    if s < 2:
        print('소수가 아닙니다')
        return
    for i in range(2,s):
        if s % i == 0:
            print('소수가 아닙니다')
            return
        else:
            print('소수입니다')
            return

prime(s)


# 6323 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 4
n = 10
lst = []

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

lst = [fibo(i) for i in range(1,n+1)]
print(lst)
print()

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

# 6326 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 7
N = 5

def fac(N):
    if N <= 1:
        return 1
    else:
        return N * fac(N - 1)

print(fac(N))


# 6327 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 8
squ = 2,3

def square(s):
    return s * s

for s in squ:
    print(f'square({s}) => {square(s)}')


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

# 6329 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 함수 10
def countdown(c):
    if c <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        while c >= 1:
            print(c)
            c -= 1

countdown(0)
countdown(10)


# 6308 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 내장함수 1
name = '홍길동'
age = 20
y = 2019 + (100 - age)

print(f'홍길동(은)는 {y}년에 100세가 될 것입니다.')


# 6311 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 내장함수 4
str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

print(sum(map(lambda x : ord('E') - ord(x), str)))


# 6312 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 내장함수 5
mul = 1,2,'4',3

def mUlti(a,b,c,d):
    return a,b,c,d

try:
    mUlti(mul)
except TypeError:
    print('에러발생')