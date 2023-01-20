# 다른 분의 문제 해결 "팁" : 2진법으로 봤을 때, 가장 오른쪽에 처음 나오는 0을 1로 바꾸고 그 바로 오른쪽 자리를 0으로 바꾸면 조건에 만족하는 수가 됩니다..!!
# (ex) 101111 -->> 110111
# (0이 없는 경우 ex) 111 -->> 1011
# (첫자리가 0인 경우 ex) 110 -->> 111, 100 -->> 101

# another solution
def f(n):
    answer = ""
    bin_n = bin(n)[2:]
    if "0" not in bin_n: # -->> n을 이진수로 변환했을 때 0이 없는 경우..!!
        # (ex) 1111 -->> 10111
        answer = "10" + bin_n[1:]
        return int(answer, 2)
    if bin_n[len(bin_n) - 1] == "0": # -->> n을 이진수로 변환했을 때 첫자리가 0인 경우..!!
        # 이 경우엔 그냥 1을 더해주면 됩니다..!!
        # (ex) 110 -->> 111
        return n + 1
    idx = 0
    for i in range(len(bin_n) - 1, -1, -1): # 위의 두 경우가 아닌 경우일 때..!!
        # 가장 오른쪽에 처음 나오는 0을 1로 바꾸고 그 바로 오른쪽 자리를 0으로 바꾸면 조건에 만족하는 수가 됩니다..!!
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
