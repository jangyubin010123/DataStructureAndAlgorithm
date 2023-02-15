
# my solution

# my thoughts : "문제 설명 중 "자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다"부분을 유의해서 문제를 풀면 될 것 같습니다..!!"

from collections import defaultdict

def solution(str1, str2):
    answer = 0
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            k = str1[i] + str1[i + 1]
            k = k.lower()
            d1[k] += 1
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            k = str2[i] + str2[i + 1]
            k = k.lower()
            d2[k] += 1
    # print(d1, d2)
    # 출력결과 Ex : defaultdict(<class 'int'>, {'fr': 1, 'ra': 1, 'an': 1, 'nc': 1, 'ce': 1}) defaultdict(<class 'int'>, {'fr': 1, 're': 1, 'en': 1, 'nc': 1, 'ch': 1})
    if len(d1) == 0 and len(d2) == 0:
        return 1 * 65536
    intersection = set(d1.keys()) & set(d2.keys())
    union = set(d1.keys()) | set(d2.keys())
    # print(intersection, union)
    # 출력결과 Ex : {'ha', 'nd', 'ds', 'ak', 'an', 'ke', 'sh'} {'ha', 'nd', 'ds', 'ak', 'an', 'ke', 'sh'}
    a1 = 0
    a2 = 0
    for i in intersection:
        a1 += min(d1[i], d2[i])
    for u in union:
        a2 += max(d1[u], d2[u])
    answer = int((a1 / a2) * 65536)
    return answer

# print(solution("aa1+aa2", "AAAA12"))
# 출력결과 Ex : 43690
