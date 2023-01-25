# my solution1 

def solution(n):
    arr = [[0] * n for _ in range(n)]
    go = n
    s = [0,0]
    v = 1
    while True:
        if go == 0:
            break
            
        # <step 1>
        for _ in range(0, go):
            arr[s[0]][s[1]] = v
            s[0] += 1
            v += 1
        s[0] -= 1 # <<-- s[0] 부분 인덱스 재조정 실시..!!
        v -= 1 # <<-- 값 재조정 실시..!!
        go -= 1 # <step 2>로 가기위한 준비..!!
        if go == 0:
            break
            
        # <step 2>
        for _ in range(0, go):
            s[1] += 1
            v += 1
            arr[s[0]][s[1]] = v 
        go -= 1 # <step 3>로 가기위한 준비..!!
        if go == 0:
            break
        
        # <step 3>
        for _ in range(0, go):
            s[0] -= 1
            s[1] -= 1
            v += 1
            arr[s[0]][s[1]] = v
        go -= 1 # 다시 <step 1>으로 가기위한 준비..!!
        if go == 0:
            break
        s[0] += 1
        v += 1
    
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                break
            else:
                answer.append(arr[i][j])
    
    return answer
        

# print(solution(6)) # <<-- 검증 완료..!!
