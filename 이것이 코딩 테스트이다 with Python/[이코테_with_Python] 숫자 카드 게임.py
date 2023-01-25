# <3> 숫자 카드 게임

# my solution
"""
n, m = map(int, input().split())

mins = []

for _ in range(n):
    row = list(map(int, input().split()))
    mins.append(min(row))

print(max(mins))
"""
# "문제 해설"
# 그리디 알고리즘 유형의 문제는 문제 해결을 위한 아이디어를 떠올렸다면 정답을 찾을 수 있다.
# -->> 이 문제를 푸는 아이디어는 바로 "각 행마다 가장 작은 수를 찾은 뒤에 -->> 그 수 중에서 가장 큰 수"를 찾는 것이다.
# 이 문제는 문제 설명이 길어서 지문 이해에 시간이 많이 소요될 수 있지만, 문제의 아이디어를 떠올리는 것은 쉬운 문제에 속한다.
# ....
# 다만, 이 문제를 해결하기 위해서는 리스트에서 가장 작은 원소를 찾아주는 min() 함수를 이용할 수 있거나,
# 2중 반복문 구조를 이용할 수 있어야 한다.
# ....

# 3-3.py min() 함수를 이용하는 답안 예시
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    # "가장 작은 수"들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
"""

# 3-4.py 2중 반복문 구조를 이용하는 답안 예시
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10_001
    for a in data:
        min_value = min(min_value, a)
    # "가장 작은 수"들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력
"""
