

# my solution1 : "시간초과"를 예상하고 그냥 작성해본 코드..!!!
"""
# -->> 역시나 문제의 조건에서 n이 20이하의 자연수라고 하였으므로 20!을 감당할 수 없게 되는듯..!!

from itertools import permutations

def solution(n, k):
    answer = []
    first_case = list(range(1, n + 1))
    all_cases = list(map(list, permutations(first_case, n)))
    answer = all_cases[k - 1]
    return answer
"""

# my solution2 : "재귀"를 이용한 풀이입니다..!!
# -->> 즉, 재귀를 통해 앞자리부터 하나하나씩 구하는 방식입니다..!!

def f(n):
    if n == 1:
        return 1
    answer = 1
    for i in range(2, n + 1):
        answer *= i
    return answer

def recursion(answer, n, k, rns):
    # rns : remained numbers
    # -->> 즉, 남은 숫자들을 의미합니다..!!
    if n == 0:
        return
    
    q = k // f(n - 1)
    r = k % f(n - 1)
    
    answer.append(rns[q]) # <<-- 실제로 우리는 q를 인덱스로 활용하면서 문제를 풀고 있기 때문입니다..!!
    del rns[q]
    
    recursion(answer, n - 1, r, rns)
    

def solution(n, k):
    k -= 1 # <<-- 문제에서 주어진 k는 인덱스 번호가 아니라 몇번째인지를 나타내는 변수이기 때문에 실제로 정답을 구하는 과정에서는 -1 처리를 해주고 재귀를 돌려야 합니다..!!
    answer = []
    rns = list(range(1, n + 1))
    recursion(answer, n, k - 1, rns)
    return answer
