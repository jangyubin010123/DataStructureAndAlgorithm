# Hint > use the "stack"..!! 
def solution(s):
    answer = -1
    stack = []
    for c in s:
        stack.append(c)
        
        if len(stack) >= 2:
            if stack[-1] == stack[-2] : 
                stack.pop()
                stack.pop()
            else : 
                continue
    if len(stack) == 0:
        answer = 1
    else : 
        answer = 0
    return answer
