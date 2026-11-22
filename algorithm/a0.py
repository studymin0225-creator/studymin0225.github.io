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