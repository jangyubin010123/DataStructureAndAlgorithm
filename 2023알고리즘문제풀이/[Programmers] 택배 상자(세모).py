# my solution : 풀긴 풀었지만 문제에 대한 설명을 완전히 이해하기 까지 너무 오래 걸린 것 같다..!!
# -->> 다음에 다시 한번 풀어봐야할 문제인 것 같다..!!

# "입출력 예시1"을 통해 유추할 수 있는 것들..!!
#   1-1. 즉, 초기상황에서 영재 앞에 놓인 상자의 번호가 영재가 실어야 하는 상자의 번호보다 작다면 보조 컨테이너 벨트(스택)에 넣어준다.
#   1-2. 만약 1-1의 상황과는 달리 영재 앞에 놓인 상자의 번호가 더 크다면 작은 번호의 상자들이 이미 스택에 들어간 상황일 것이므로 이때는 스택에서 확인해준다..!!
#   1-3. 1-2를 진행하되 영재가 실어야 하는 상자 번호와 스택의 최상단에 있는 상자 번호가 다르다면 이때는 영재가 더이상 상자를 실을 수 없다는 뜻이므로 결괏값을 반환해준다..!!

# "입출력 예시2"를 통해 유추할 수 있는 것들..!!
#   2-1. 스택에 있는 상자들과 비교하기도 전에 즉, 1-3의 상황에 가기도 전에 컨테이너 벨트에 비교할 상자가 1개도 없는 상황이 된다면 이때는
# 스택에서 비교하고 두 상자의 번호가 다르면 바로 결괏값을 반환해주면 된다..!!

from collections import deque

def solution(order):
    answer = 0
    cb = deque(list(range(1, len(order) + 1))) # 컨테이너 벨트를 의미하며 영재 앞에 놓이게 될 상자의 번호를 순차적을 나타낸 것
    stack = [] # 보조 컨테이너의 설치
    idx = 0 # 영재가 (현재) 실어야 하는 상자의 번호를 가리키기 위해 인덱스를 설정함..!!
    while cb:
        if order[idx] == cb[0]:
            cb.popleft()
            idx += 1
            answer += 1
        elif order[idx] > cb[0]:
            stack.append(cb.popleft())
        elif order[idx] < cb[0]:
            # 참고 > 이 구문을 만족했다는 것은 영재 앞에 놓인 상자의 번호가 영재가 실어야 하는 상자의 번호보다 큰 상황이라는 것이고 이때는 스택에 영재 앞에 놓인 상자의 번호보다 작은 상자들이 있다는 뜻이므로 이때는 스택에서 비교해주면 된다..!!
            if stack[-1] == order[idx]:
                stack.pop()
                idx += 1
                answer += 1
            else: 
                return answer
    
    while stack and idx <= len(order) - 1:
        if order[idx] == stack[-1]:
            stack.pop()
            idx += 1
            answer += 1
        else:
            break
    
    return answer


# print(solution([5,4,3,2,1]))
