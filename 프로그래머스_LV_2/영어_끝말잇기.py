def solution(n, words):
    answer = [0, 0] # <<-- 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.
    counting = [0] * n # <<-- 각각의 사람들이 몇 번의 끝말잇기를 수행했는지 counting 해주는 리스트의 선언입니다..!!
    stack = [] # <<-- 여태까지 나왔던 단어들을 저장해주는 stack 즉, 리스트이자 스택의 선언이라고 보시면 됩니다..!!
    
    for i in range(0,len(words)):
        if i == 0:
            stack.append(words[i])
            counting[i] += 1
            continue # <<-- continue를 꼭 넣어줘야 합니다..!!
            # 만약 continue 문을 안넣어주면 아래 문장까지 수행하게 되어서 원하는 결괏값이 나오지 않음..!!
        
        if words[i] not in stack and words[i][0] == stack[-1][-1]:
            counting[i % n] += 1
            stack.append(words[i])
        else:
            counting[i % n] += 1
            answer[0] = i % n  +1
            answer[1] = counting[i % n]
            break
            
    return answer
