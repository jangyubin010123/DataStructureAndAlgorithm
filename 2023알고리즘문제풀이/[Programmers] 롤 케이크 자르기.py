# my solution1
"""
def solution(topping):
    answer = 0
    for i in range(len(topping)):
        if len(set(topping[0:i+1:1])) == len(set(topping[i+1::1])): # -->> 이 부분이 "시간초과"의 원인..!! -->> 매번 반복할 때마다 set() 처리를 하면서 "시간초과"가 걸린 것으로 예상..!!
            answer += 1
    return answer
"""

# my solution2 : "딕셔너리 자료형"을 통해 "시간 초과"를 해결한 풀이 방법입니다..!!
"""
def solution(topping):
    answer = 0
    d2 = dict() # 초기에 동생이 가지고 있는 토핑들..!!
    for t in topping:
        if t not in d2:
            d2[t] = 1
        else:
            d2[t] += 1
    d1 = dict() # 앞으로 철수가 차지하게 될 토핑들..!!
    # -->> 즉, 철수가 하나씩 토핑을 뺏는 방식으로 생각하면 됩니다..!!
    # -->> 즉, 철수가 가지게 될 토핑들 : d1
    # -->> 즉, 동생이 가지고 있는 토핑들 : d2
    
    for t in topping:
        if t not in d1:
            d1[t] = 1
        else:
            d1[t] += 1
        
        d2[t] -= 1
        if d2[t] == 0:
            del d2[t]
        
        if len(d1.keys()) == len(d2.keys()):
            answer += 1
        elif len(d1.keys()) > len(d2.keys()):
            break # -->> 계속 하나씩 동생 것을 뺏으면서 진행하다가 철수가 더 많은 토핑을 가지는 순간부터는 비교할 필요가 없기 때문입니다..!!

    return answer

# print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
"""

# another solution1 : 파이썬 "collections" 모듈의 "Counter"클래스를 활용한 풀이입니다..!!
# 참고 > 파이썬 collections 모듈의 Counter 클래스 관련해서 참조한 사이트
# -->> "https://www.daleseo.com/python-collections-counter/"
from collections import Counter

def solution(topping):
    answer = 0
    be_ = set()
    af = Counter(topping)

    for t in topping:
        be_.add(t)
        af[t] -= 1

        if af[t] == 0:
            del af[t]
        if len(be_) == len(af):
            answer += 1

    return answer
