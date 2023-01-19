# my solution
def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i-1]% 1_000_000_007) + (dp[i-2]% 1_000_000_007)
        dp[i] %= 1_000_000_007
    answer = dp[n]
    return answer

# my thoughts : 이 문제의 key point는 문제의 조건에 맞게 알맞은 점화식을 찾는 것입니다..!!
