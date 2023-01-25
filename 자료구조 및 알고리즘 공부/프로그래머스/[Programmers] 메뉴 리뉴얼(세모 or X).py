# my solution1 (X) -->> "완전탐색"을 돌면서 교집합을 구하면 안된다..!! "ABCD" 와 "ABCD"를 비교할 때 만약 "스카피"가 2가지로 구성된 단품메뉴 조합을 만들려고 하면 예외가 발생하기 때문입니다..!!
# -->> 즉, 이렇게 나옵니다.!!
# -->> 	"실행한 결괏값 ["ABCD"]이 기댓값 ["AB","ABC","ABCD","ABD","AC","ACD","AD","BC","BCD","BD","CD"]과 다릅니다."
"""
def solution(orders, course):
    answer = []
    # <step 1> 일단 "완전탐색"을 하면서 함께 주문된 메뉴 구성이 길이가 2 이상이면서 그 길이가 course안에 있는 메뉴 구성을 선별한다..!!
    candidates = []
    for i in range(0, len(orders) - 1):
        for j in range(i + 1, len(orders)):
            temp = list(set(orders[i]) & set(orders[j]))
            temp.sort() # <<-- "배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다."
            temp = "".join(temp)
            if len(temp) not in course:
                continue
            # print(temp) <<-- 여기까지 ok..!!
            if temp not in candidates:
                candidates.append(temp)
    # print(candidates) <-- 여기까지 ok..!!
    # <step 2> 이제 candidates배열에 들어간 메뉴 구성 후보들 중에 각각의 후보가 몇번 등장했는지 counting 해야 됩니다..!!
    count = dict()
    for c in candidates:
        count[c] = 0
    
    for c in candidates:
        for order in orders:
            temp = set(c) & set(order)
            if len(temp) != len(c):
                continue
            else:
                count[c] += 1
    # print(count) -->> 출력결과 Ex : {'AB': 2, 'CD': 3, 'ADE': 2, 'ACD': 2, 'AD': 3, 'XYZ': 2}
    # <step 3> 이제, 마지막으로 선별하는 작업을 거쳐서 답을 반환합시다..!!
    check = [[] for _ in range(max(course) + 1)]
    # print(check) -->> 출력결과 Ex : [[], [], [], [], [], []]
    for k, v in count.items():
        check[len(k)].append((k, v))
    # print(check) -->> 출력결과 Ex : [[], [], [('AB', 2), ('CD', 3), ('AD', 3)], [('ADE', 2), ('ACD', 2), ('XYZ', 2)], [], []]
    for i in range(len(check)):
        check[i].sort(key = lambda x : x[1], reverse = True)
    # print(check) -->> 출력결과 Ex : [[], [], [('CD', 3), ('AD', 3), ('AB', 2)], [('ADE', 2), ('ACD', 2), ('XYZ', 2)], [], []]
    for i in range(len(check)):
        if len(check[i]) == 0:
            continue
        for j in range(len(check[i])):
            if check[i][0][1] != check[i][j][1]:
                break
            answer.append(check[i][j][0])
    # print(answer) <<-- 여기까지 ok..!!
    answer.sort() # <<-- 사전순 정렬 시행..!!
    return answer
'''
해당 테스트 케이스를 돌려보세요.

solution(["ABCD", "ABCD", "ABCD"], [2,3,4])

답 :
["AB", "ABC", "ABCD", "ABD", "AC", "ACD", "AD", "BC", "BCD", "BD", "CD"]
'''
"""

# my solution2 : "조합"을 이용한 풀이입니다..!!

from itertools import combinations

def solution(orders, course):
    answer = []
    d1 = dict() # <<-- 가능한 조합들과 그 조합이 나온 횟수를 counting 해주는 딕셔너리 자료형 d1입니다..!!
    # <<-- d1에서는 해당 조합이 나온 횟수가 1인 것도 포함됩니다..!! <<-- 따라서, 나중에 d2를 통해 선별되는 과정을 거쳐야 합니다..!!
    for order in orders:
        for num in course:
            temp = list(map(list, combinations(order, num)))
            for t in temp:
                t.sort() # <<-- "배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다."
                t = "".join(t)
                if t not in d1:
                    d1[t] = 1
                else:
                    d1[t] += 1
    
    d2 = dict() # <<-- d1에서 나온 조합들 중 나온 횟수가 1인 조합은 제외하고 남은 것들을 담은 딕셔너리 자료형 d2입니다..!!
    # 나온 횟수가 1인 조합들을 제외시켜야 하는 이유는 나온 횟수가 1이라는 것은 한명만 그 조합을 포함하여 음식을 주문했다는 의미이기 때문입니다..!!
    for k, v in d1.items():
        if v == 1:
            continue
        else:
            d2[k] = v
    l = [[] for _ in range(max(course) + 1)]
    # 참고 > 여기서 l리스트의 인덱스 는 문자열의 길이를 의미하게 됩니다..!!
    # print(l) # 출력결과 Ex : [[], [], [], [], [], []]
    #                              길이가 1인 조합들이 담길 리스트의 위치입니다..!!
    for k, v in d2.items():
        l[len(k)].append((k, v))
    for i in range(len(l)):
        l[i].sort(key = lambda x : x[1], reverse = True)
    # print(l) # 출력결과 Ex : [[], [], [('AC', 4), ('CD', 3), ('CE', 3), ('DE', 3), ('BC', 2), ('BF', 2), ('BG', 2), ('CF', 2), ('CG', 2), ('FG', 2), ('AD', 2), ('AE', 2)], [('CDE', 3), ('BCF', 2), ('BCG', 2), ('BFG', 2), ('CFG', 2), ('ACD', 2), ('ACE', 2), ('ADE', 2)], [('BCFG', 2), ('ACDE', 2)]]
    for i in range(len(l)):
        if len(l[i]) == 0:
            continue
        for j in range(len(l[i])):
            if l[i][0][1] != l[i][j][1]:
                break
            answer.append(l[i][j][0])
    
    answer.sort() # <<-- "정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요."
    return answer
