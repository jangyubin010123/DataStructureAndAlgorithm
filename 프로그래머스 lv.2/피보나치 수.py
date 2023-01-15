# 참고 > '재귀 함수'를 이용하면 '시간초과' 판정을 받을 것임..!!
# -->> 즉, 다른 풀이를 고려해봐야함..!!
def solution(n):
    answer = 0
    f0 = 0
    f1 = 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        pass
    
    for i in range(n - 2):
        f0, f1 = f1, f0 + f1
    answer = (f0 + f1) % 1234567
    
    return answer
