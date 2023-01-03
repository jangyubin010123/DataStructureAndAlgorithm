# 문제 설명 中 : 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.

# my solution 
"""
def solution(s):
    answer = 0
    # "Two Pointer" 이용..!!
    left = 0
    compare = 0 
    while left <= len(s) - 1:
        if left == len(s) - 1:
            answer += 1
            break # <==> 'return answer' 라고 작성해도 됩니다..!!
        compare = 1
        for right in range(left+1, len(s)):
            if right == len(s) - 1:
                answer += 1
                return answer # -->> 문제 조건 中 3번째 조건을 만족시키기 위해서..!!
            
            if s[left] == s[right] :
                compare += 1
            else :
                compare -= 1
            if compare == 0:
                answer += 1
                left = right + 1
                break
    return answer
"""

# another solution
from collections import deque

def solution(s):

    ans = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return ans
