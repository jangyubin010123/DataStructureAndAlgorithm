# my thoughts : 한칸씩 내려갈 때마다 받을 수 있는 값과 자신이 갖고 있는 값의 합의 최댓값을 저장하는 방식으로 접근..!! -->> "보텀업(Bottom-Up)"방식을 활용한 풀이입니다..!!

# my solution1

def solution(triangle):
    answer = 0
    # dp 테이블 준비
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    # print(dp) # 출력결과 Ex : 	[[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
    dp[0] = triangle[0]
    # print(dp[0])
    for i in range(1, len(triangle)):
        for j in range(0, i + 1):
            if j == 0: # <<-- 이때는 자기 자신을 기준으로 대각선 오른쪽 위에서 밖에 못받음..!!
                dp[i][0] = triangle[i][0] + dp[i-1][0]
                continue
            if j == i: # <<-- 이때는 자기 자신을 기준으로 대각선 왼쪽에서 밖에 못받음..!!
                dp[i][j] = triangle[i][j] + dp[i-1][j - 1]
                continue
            
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    # print(dp)
    answer = max(dp[len(triangle) - 1])
    return answer

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
