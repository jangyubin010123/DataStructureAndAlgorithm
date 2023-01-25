# my solution

from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    l = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    # 참고 while문 안에 "sum()" 처리를 하게되면 연산횟수가 비약적으로 상승하게 되어서 "시간초과"를 받는다..!! -->> 따라서 초기에 한 번만 해주고 작업을 하면서 그때그때마다 더하거나 빼주는 식으로 작업을 진행해서 연산 횟수를 줄여야 합니다..!!
    
    count = 0
    while queue1 and queue2: # -->> 두 큐의 합이 같지 않은 상황에서 어느 한쪽의 큐가 비게 된다면 더 이상의 작업은 무의미하기 때문에 작업을 중단해주고 "return -1" 처리를 해주면 됩니다..!!
    # -->> 기본적인 알고리즘은 매 작업마다 두 큐의 합을 비교해서 어느 한쪽이 더 크면 큰 쪽에서 숫자 하나를 빼서 작은 쪽에 추가하는 식으로 진행하는 것입니다..!!
        if sum1 == sum2:
            return count
        if count >= 4 * l:
            # -->> 즉, 작업을 초기 길이의 4배만큼 돌면 초기 상태로 큐가 다시 만들어지므로 더 작업을 반복해봤자 의미없는 작업이됨..!!
            # 참고 > 2 * l 만큼 돌면 queue1 -->> queue2 , queue2 -->> queue1로 바뀌긴 하나 반례가 생길 수 있으므로 안전하게 4 * l 만큼 돌아줍시다..!!
            return -1
        
        if sum1 > sum2:
            value1 = queue1.popleft()
            queue2.append(value1)
            sum1 -= value1
            sum2 += value1
            count += 1
        elif sum1 < sum2:
            value2 = queue2.popleft()
            queue1.append(value2)
            sum2 -= value2
            sum1 += value2
            count += 1
    
    return -1

# 참고 > 정말로 "4*l" 만큼 돌면 초기 큐 상태로 돌아가는가..??
# (ex) queue1 = [1, 2, 4]
#      queue2 = [3, 2, 4]
# 2*l번 작업을 수행하고 난 후 두 큐의 상태 : queue1 = queue2, queue2 = queue1
# 4*l번 작업을 수행하고 난 후 두 큐의 상태 : queue1 = queue1, queue2 = queue2
