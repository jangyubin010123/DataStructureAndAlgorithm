# my solution1 (X) <<-- why..?? -->> Because of "시간초과"..!!
"""
def solution(n):
    answer = ''
    dp = [1] * (n + 1)# 보텀업 방식으로 문제를 풀 때 이용할 수 있는 Dp테이블입니다..!!
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        while True:
            checkFlag = True
            for c in str(dp[i]):
                if c not in "124":
                    checkFlag = False
                else:
                    continue
            if checkFlag == True:
                break
            else:
                dp[i] += 1
    answer = str(dp[n])           
    return answer
"""

# my solution2 (O) : "3진법"을 활용한 풀이..!!

def From10To124(n): # 참고 > "3진법"을 이용하되 124나라에 맞게 변형하는 과정을 추가로 해줍시다..!!
    answer = ""
    
    while n != 0: # <<-- 즉, n이 1일때 까지만 해야되기 때문입니다..!!
        n, digit = divmod(n, 3)
        if digit == 0:
            digit += 4
            n -= 1
        answer += str(digit)
    answer = answer[-1::-1]
    return answer

def solution(n):
    answer = From10To124(n)
    return answer

# my thoughts : 문제의 조건 중에서 124나라에는 모든 수를 표현할 때 1, 2, 4만 사용한다고 하였으므로 "3진법"과 유사한 메커니즘을 사용한다는 것을 유추할 수 있습니다. 즉, "3진법"을 활용하되 "0"이라는 숫자가 나올 때 "4"로 변형해주는 작업을 해주는 것이 key point인것 같습니다..!!
