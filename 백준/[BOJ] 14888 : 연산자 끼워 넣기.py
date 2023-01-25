# <Q19> 연산자 끼워 넣기

# my solution

import sys
from itertools import permutations

n = int(input())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
op = ["+", "-", "*", "//"]
op_count = list(map(int, sys.stdin.readline().rstrip().split()))
ops = []

for i in range(0, 4):
    ops += [op[i]] * op_count[i]
# print(ops) <<-- 여기까지 ok..!!

cases = list(permutations(ops, n - 1))
cases = list(set(cases))
# print(len(cases)) <<-- 여기까지 ok..!!

answer_list = []

for case in cases:
    answer = nums[0]
    for i in range(0, n-1):
        if case[i] == "+":
            answer += nums[i + 1]
        elif case[i] == "-":
            answer -= nums[i + 1]
        elif case[i] == "*":
            answer *= nums[i + 1]
        elif case[i] == "//":
            if answer < 0:
                answer = -1 * answer
                answer //= nums[i + 1]
                answer = - 1* answer
                continue
            answer //= nums[i + 1]
    # if answer == 54:
    #    print(case)
    # if answer == -24:
    #    print(case)
    answer_list.append(answer)

max_answer = max(answer_list)
min_answer = min(answer_list)
print(max_answer)
print(min_answer) # <<-- 마지막에 최댓값과 최솟값을 차례대로 출력해줍시다..!!

# <A19> 연산자 끼워 넣기
# 이 문제는 최대 11개의 수가 주어졌을 때, 각 수와 수 사이에 사칙연산 중 하나를 삽입하는 모든 경우에 대하여 만들어질 수 있는 최댓값과 최솟값을 구하면 된다.
# 따라서 모든 경우의 수를 계산하기 위하여(완전 탐색) DFS 혹은 BFS를 이용하여 문제를 해결할 수 있다.
# 이 문제에서는 각 사칙연산을 중복하여 사용할 수 있기 때문에, 이 문제를 풀기 위해서는 중복 순열을 계산해야 한다.
# 예를 들어 n = 4라고 하면, 사칙연산 중에서 중복을 허용하여 3개를 뽑아 나열하는 모든 경우를 고려해야 한다.
# 이는 파이썬에서의 중복 순열(product) 라이브러리를 이용하여 찾을 수도 있다. 아래의 예시 소스코드 또한 확인해보자.

"""
from itertools import product

n = 4
print(list(product(["+", "-", "*", "//"], repeat = (n - 1))))
"""

# 참고 > 452p "itertools"
# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.
# 제공하는 클래스는 매우 다양하지만, 
# 코딩 테스트에서 가장 유용하게 사용할 수 있는 클래스는 permutations, combinations이다.
# 참고로 순열과 조합에 대한 설명은 부록 B에서도 추가로 다루고 있다.
# ....
# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산해준다.
# 다만 원소를 중복하여 뽑는다. -->> "그래서 보통 '중복 순열'이라고 부르곤 합니다..!!"
# -->> "product 객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어줍니다..!!"
# product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
# 리스트 ['A', 'B', 'C']에서 중복을 포함하여 2개(r = 2)를 뽑아 나열하는 모든 경우를 출력하는 예시는 다음과 같다.

"""
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result) # 출력 결과 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
"""

# 다만, 본 문제에 대한 정답 소스코드는 itertools의 중복 순열(product) 클래스를 사용하지 않고 DFS를 이용하여 푸는 방법을 소개하겠다.

# A19.py 답안 예시
# ....
# .... # <<-- 책에 있으니 참고할 것..!!
