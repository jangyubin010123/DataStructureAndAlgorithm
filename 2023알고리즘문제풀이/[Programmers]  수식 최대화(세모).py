# my solution2

# my thoughts : 처음에는 연산자와 숫자를 분리하지 않고 풀려고 하였으나 너무 코드가 복잡해서 구글링을 참조하였더니 숫자와 연산자를 분리하면서 푼 부분에서 힌트를 얻었음..!!

from itertools import permutations
import re

def solution(expression):
    answer = 0
    answer_list = []
    cases = list(permutations(['*', '-', '+'], 3))
    
    for case in cases:
        nums = re.findall("[0-9]+", expression)
        operators = re.findall("[+*-]",expression)
        for op in case:
            i = 0
            while i <= len(operators) - 1:
                if operators[i] == op:
                    # 참고 > 이 구문("if operators[i] == op:")에서는 어차피 연산 완료 후
                    # operators 연산자 하나가 사라져야 하므로 else 구문처럼 "i+=1" 처리를 할 필요가 없습니다..!!
                    temp = str(eval(nums[i] + operators[i] + nums[i+1]))
                    nums[i] = temp
                    del nums[i+1]
                    del operators[i]
                else:
                    i += 1
        answer_list.append(abs(int(nums[0])))

    answer = max(answer_list)
    return answer

# print(solution("100-200*300-500+20"))
