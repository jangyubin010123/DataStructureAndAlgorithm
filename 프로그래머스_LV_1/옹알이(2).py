# my solution
def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    temp = []
    for word in babbling:
        for c in can:
            if c in word and c*2 not in word: # 즉, 2개가 연속으로 존재하면 안되기 때문에 "c*2 not in word"를 작성하였습니다..!!
                word = word.replace(c,"0")
                # print(word)
                # print(babbling) -->> But, 기존 배열은 값 변경 x..
        temp.append(word)
        print(temp) # <<-- 여기까지 ok..!!
    
    for t in temp:
        t = t.replace("0","")
        if len(t) == 0:
            answer += 1
        else:
            continue
    
                
                
    return answer

# another solution
"""
추후 올릴 예정..!!"""
