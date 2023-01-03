# 제한사항 : 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
# my solution
"""
def solution(X, Y):
    answer = ''
    dict_x = {}
    dict_y = {}
    for x in X:
        if x not in dict_x:
            dict_x[x] = 1
        else:
            dict_x[x] += 1
    for y in Y:
        if y not in dict_y:
            dict_y[y] = 1
        else:
            dict_y[y] += 1
    # print(dict_x)
    # print(dict_y) # <<-- X,Y에 대해서 각각 딕셔너리 자료형 구축 완료..!!
###############################################################################    
    for k in dict_x:
        if k in dict_y: # 즉, 공통으로 존재한다면..!!
            answer += k * min(dict_x[k],dict_y[k])
        else:
            continue
    # print(answer) <<-- 여기까지 ok..!!
    answer = list(answer)
    answer.sort(reverse = True) # 내림차순 정렬..!!
    answer = "".join(answer)
    print(answer)
    if len(answer) == 0:
        return "-1"
    if answer[0] == '0': # 즉, 앞자리가 0이라는 뜻은 "0000" 이런식으로 존재한다는 뜻이므로 "0"으로 변환해줘야 함..!!
        answer = "0"
        
    return answer
"""

# another solution
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif answer[0] == "0":
        return '0'
    else :
        return answer
