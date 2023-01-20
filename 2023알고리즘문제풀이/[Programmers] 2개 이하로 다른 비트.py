# another solution

# <Tip>
"""
2진법으로 봤을때,
가장 오른쪽에 처음으로 나오는 0을 1으로 바꾸고
그 바로 오른쪽 자리를 0으로 바꾸면 조건에 만족하는 수가 됩니다.
ex) 101111 -> 110111
0이 없는경우) 111 -> 1011
첫자리가 0인경우) 110 -> 111, 100 -> 101
"""

def f(n):
    answer = ""
    bin_n = bin(n)[2:]
    if "0" not in bin_n:
        answer = "10" + bin_n[1:]
        return int(answer, 2)
    if bin_n[len(bin_n) - 1] == "0":
        return n + 1
    idx = 0
    for i in range(len(bin_n) - 1, -1, -1): 
        if bin_n[i] == "0":
            idx = i
            break
    answer = bin_n[0:idx:1] + "1" + "0" + bin_n[idx+2::1]
    return int(answer, 2)
    
def solution(numbers):
    # print(int("111",2))
    answer = [f(number) for number in numbers]
    return answer

# print(solution([2,7]))

# my solution(X) : "시간초과" 판정...!!!
