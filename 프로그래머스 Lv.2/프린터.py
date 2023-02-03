# my solution

# 참고1 > -->> "인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다."
# 참고2 > -->> "location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다." -->> "즉, 인덱스 값을 의미합니다..!!"

from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((p, i))
        
    while queue: # <<-- 큐가 빌 때까지 반복해주면 됩니다..!!
        cur_p, cur_i = queue.popleft() # <<-- 현재 확인해야할 문서의 중요도와 기존 인덱스값..!!
        checkFlag = True # <<-- 현재 확인 중인 문서가 인쇄 작업에 들어가야할 문서인지 아닌지 나타내는 변수입니다..!!
        
        for i in range(len(queue)): # <<-- 큐에 남아있는 문서들의 중요도보다 크거나 같다면 현재 확인 중인 문서는 인쇄 작업에 들어가야 합니다. 하지만, 큐에 남아있는 문서들의 중요도보다 작다면 현재 확인 중인 문서는 인쇄 작업에 들어가면 안되므로 큐 뒷쪽에 다시 넣어줘야 합니다..!!
            if cur_p >= queue[i][0]:
                continue
            else:
                queue.append((cur_p, cur_i))
                checkFlag = False
                break
        
        if checkFlag == True: # <<-- 현재 확인 중인 문서가 인쇄 작업에 들어가야 하는 경우..!!
            if cur_i == location: # <<-- 현재 인쇄 작업에 들어가야 하는 문서가 내가 인쇄를 요청한 문서가 맞다면..!!
                answer += 1
                return answer
            else: # <<-- 그렇지 않다면..!!
                answer += 1
            
    return answer
