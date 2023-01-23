# my solution

def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        if not stack or k == 0: # <<-- 즉, 스택이 비어있거나 더 이상 숫자를 제거할 수 없는 상황이라면 스택에 숫자를 그냥 append 해줘야 합니다..!!
            stack.append(num)
            continue
        
        while int(num) > int(stack[-1]) and k > 0: # <<-- 즉, 해당 num이 스택의 최상단보다 크고 아직 제거할 수 있는 상황이라면 스택의 최상단에서부터 하나씩 차근차근 빼주면(제거해주면) 됩니다..!!
            stack.pop()
            k -= 1
            if not stack: 
                break
        
        stack.append(num)
    
    # 만약 while문을 끝낸 후에도 k가 양수인 상태라면 아직 우리는 숫자를 제거해야 한다는 뜻이고 즉, stack 자료구조의 상단쪽에서 k개 제거해야 한다는 뜻입니다..!!
    # -->> Q. why 최상단 부분에서부터 제거해야 하는가..?
    # -->> A. Beacause 스택의 최하단에는 가장 큰 숫자가 들어가 있는 상태이기 때문입니다..!!
    if k > 0:
        stack = stack[0:len(stack) - k]
    
    # print(stack) # -->> 출력결과 Ex : ['7', '7', '5', '8', '4', '1']
    answer = "".join(stack)
    return answer
