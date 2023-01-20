# my solution1 -->> "시간초과" 판정..!!
"""
def solution(weights):
    w = weights
    w.sort(reverse = False)
    # print(w)
    answer = 0
    check = {1/2, 2/3, 3/4, 1}
    for i in range(0, len(w) - 1):
        for j in range(i+1, len(w)):
            if w[i]/w[j] < 1/2:
                break
            if w[i]/w[j] in check:
                # print(w[i]/w[j])
                answer += 1
    return answer
"""

# my solution2

# 문제에서 내가 잘못 이해한 부분 : 그저 (w1, w2)쌍이 몇쌍 존재하는 지 구하라는 문제인 줄 알았다.
# 그러나 문제에서 주어진 weights 리스트처럼 각 사람마다 각기다른 다른 번호를 부여받았으며 1번 사람과 3번 사람의 몸무게가 100, 300이고 2번 사람과 3번 사람도 몸무게가 100, 300이라고 가정하면 이 경우 총 경우의 수는 1개가 아니라 2개로 쳐야 되기 때문입니다..!!
# 참고 > 딕셔너리 자료형을 통해 완전탐색을 할 수 있는 이유는 문제의 제한 사항 중 각 사람 당 몸무게는 100이상 1000이하라고 하였으므로 딕셔너리 생성시 최악의 경우에도 키 값은 총 901가지 밖에 생성되지 않기 때문입니다..!!
# -->> 따라서 대략 81000번의 연산 밖에 수행하지 않기 때문에 "시간초과" 판정을 피할 수 있게 됩니다..!!

def solution(weights):
    answer = 0
    d = dict()
    check = {1/2, 2/3, 3/4}
    for w in weights:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    # print(d) # {100: 2, 180: 1, 360: 1, 270: 1}
    for k, v in d.items():
        if v >= 2:
            answer += v*(v-1) // 2
            # 참고 > nC2 == n(n-1) // 2
    l = list(d.keys())
    l.sort(reverse = False)
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i]/l[j] < 1/2:
                break
            if l[i]/l[j] in check:
                answer += (d[l[i]] * d[l[j]]) 
    return answer

# print(solution([100,180,360,100,270]))
            
