# <Q03> 문자열 뒤집기

# my solution1 : "정규표현식"을 이용한 풀이입니다..!!

import re

s = input()

zeros = re.findall("[0]+", s)
ones = re.findall("[1]+", s)

if len(zeros) >= len(ones):
    print(len(ones))
else:
    print(len(zeros))
    

# my solution2 : 문자열 내장 함수 ".split()"을 이용한 풀이입니다..!!
"""
s = input()
ones = s.split("1")
zeros = s.split("0")

# print(ones) # 출력결과 Ex : ['000', '', '000', '', '', '', '0000']
# print(zeros) # 출력결과 Ex : ['', '', '', '11', '', '', '1111', '', '', '', '']

count_ones = 0
for one in ones:
    if one == "":
        continue
    else:
        count_ones += 1

count_zeros = 0
for zero in zeros:
    if zero == "":
        continue
    else:
        count_zeros += 1

print(min(count_zeros, count_ones))
"""

# <A03> 문자열 뒤집기
# 다솜이는 모든 숫자를 전부 같게 만드는 것이 목적이다. 따라서 "전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산"하면 된다.
# 예를 들어 문자열이 "0001100"이라고 가정해보자.
# 이때 "모두 0으로 만드는 경우"와 "모두 1로 만드는 경우"를 고려했을 때 각각 뒤집기 횟수를 고려함녀 다음과 같다.
# ....
# ....
# 이를 실제로 구현할 때는 전체 리스트의 원소를 앞에서부터 하나씩 확인하며, 0에서 1로 변경하거나 1에서 0으로 변경하는 경우를 확인하는 방식으로 해결할 수 있다.
# 소스코드는 다음과 같다.

# A03.py 답안 예시
# ....
# ....
# ....
