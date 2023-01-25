# my solution

def IsCorrectString(s): # -->> 올바른 괄호 문자열인지 판단해주는 함수입니다..!!
    check = 0
    for i in range(len(s)):
        if s[i] == "(":
            check += 1
        else:
            check -= 1
            if check < 0 :
                return False
    if check == 0:
        return True
    # 참고 > 즉, 빈 문자열도 올바른 괄호 문자열 중 하나임..!!
    # 즉 빈 문자열이 이 함수에 들어온다면 for문을 돌지 않기 때문에
    # check == 0이 되어 "True"를 반환해줄 것입니다..!!
    
def DetachUandV(s): # -->> 새로운 u와 v로 나누어주는 함수입니다..!!
    check = 0
    for i in range(len(s)):
        if s[i] == "(":
            check += 1
        else:
            check -= 1
        
        if check == 0:
            u = s[0:i+1:1]
            v = s[i+1::1]
            return (u, v) # (u, v) 즉, 튜플 형태로 반환값을 정의해보았습니다..!!
    

def recursion(p):
    answer = ''
    if IsCorrectString(p):
        return p
    if p == "": # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = DetachUandV(p)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if IsCorrectString(u):
        # 문자열 v에 대해 1단계부터 다시 수행합니다.
        v = recursion(v)
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        u += v
        answer = u
        return answer
        
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        empty = ""
        #  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        empty += "("
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        v = recursion(v)
        # 문자열을 이어 붙입니다.
        empty += v
        # 4-3. ')'를 다시 붙입니다. 
        empty += ")"
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 
        u = u[1:len(u) - 1]
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        reversed_u = ""
        for i in range(len(u)):
            if u[i] == "(":
                reversed_u += ")"
            else:
                reversed_u += "("
        empty += reversed_u
        # 4-5. 생성된 문자열을 반환합니다.
        answer = empty
        return answer

def solution(p):
    answer = ''
    if p == "":
        return answer
    answer = recursion(p)
    return answer

# print(solution("()))((()"))
# print(solution(")("))

# <A18> 괄호 변환
# 이 문제는 제시된 알고리즘을 재귀적으로 구현하여 해결할 수 있다.
# 구현을 위한 알고리즘 자체는 문제에 그대로 제시되어 있기 때문에, 
# 재귀 함수를 이용하여 기재되어 있는 알고리즘을 실수없이 안정적으로 구현할 수 있으면 문제를 해결할 수 있다.
# -->> "엄밀히 말하면 이 문제는 DFS 문제는 아니다. 정확한 구현을 요구하고, 실수하기 쉬운 문제라는 점에서 구현 문제 유형으로 분류할 수도 있다."
# -->> "하지만 DFS 알고리즘의 핵심이 되는 재귀 함수 구현을 요구한다는 점에서 DFS 연습 목적의 문제로 DFS/BFS 파트에서 다루고자 한다."
# 이 문제를 실수 없이 풀려면 소스코드를 최대한 단순화하는 것이 좋다.
# 따라서 특정 문자열에서 "균형잡힌 괄호 문자열"의 인덱스를 반환하는 함수와 특정한 "균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"인지 판단하는 함수를 별도로 구현한다.
# 이후에 재귀 함수에서 이 두 함수를 불러오도록 소스코드를 작성할 수 있다.
