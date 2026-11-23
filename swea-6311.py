# 6311 파이썬 프로그래밍 기초 파이썬의 기본 구조와 기초 문법
# 내장함수 4
str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

print(sum(map(lambda x : ord('E') - ord(x), str)))
