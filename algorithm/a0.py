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