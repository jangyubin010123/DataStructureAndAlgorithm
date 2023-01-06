def solution(n):
    answer = 0
    temp = n
    while True:
        temp += 1
        if bin(temp)[2:].count("1") == bin(n)[2:].count("1") :
            answer = temp
            break
    return answer
