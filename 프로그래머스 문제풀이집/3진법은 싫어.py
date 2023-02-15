# my solution

# my thoughts : 
# 1. 자연수 n을 3진법으로 변환한다.
# 2. 변환된 3진법을 앞뒤로 뒤집는다.
# 3. 이를 다시 10진법으로 만든다..!!

def From10To3(n):
    answer = ""
    while n != 0:
        n, digit = divmod(n, 3)
        answer += str(digit)
    return answer

def From3To10(n):
    answer = int(n, 3) # <<-- "int(n, 3)"은 현재 n이 3진법으로 표현된 문자열이므로 이를 10진법의 정수로 변환해주는 함수입니다..!!
    return answer
    
def solution(n):
    answer = From3To10(From10To3(n))
    return answer

print(solution(45))
