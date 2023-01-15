# my solution
"""
# 참고 > 제 풀이에서 "컴파일된 패턴 객체"변수를 설정해서 유사하게 문제를 풀어나가도 됩니다..!!
import re

def solution(files):
    temp = []
    answer = []
    for i, file in enumerate(files):
        # Q. why we must use "enumerate(files)"?
        # A. Because -->> "두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다."라는 문제의 조건이 있기 때문입니다..!!
        original = file
        file = file.lower() # <<-- 이때, 문자열 비교시 대소문자 구분을 하지 않는다. 따라서 모두 소문자로 바꿔줍시다..!!
        head = re.match("[a-z .-]+", file) # 참고 > 여기서 head 는 match 객체가 됩니다..!!
        # Q. 왜 "[a-z .-]+" 라고 썼는가..??
        # A. 숫자 전까지 끊어야 하므로 '-'같은 것이 등장했을 때 포함시켜야 하기 때문입니다..!!
        # 참고 > 13행에서 "[a-z .-]+" 를 "[^0-9]+"라고 써도 됩니다..!!
        # 문제의 조건 中 -->> HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
        # print(head.group()) <<-- 여기까지 ok..!!
        # 참고 > .group() 함수는 매칭된 문자열을 반환해줍니다..!!
        file = file.replace(head.group(), "") # <<-- 잠시 숫자 부분을 빼줍시다..!!
        # print(file) <<-- 여기까지 ok..!!
        number = re.match("[0-9]+", file)
        idx = i
        temp.append((head.group(), int(number.group()), idx, original))
    
    temp.sort(key = lambda x : (x[0], x[1], x[2]))
    for t in temp:
        answer.append(t[3])
    return answer
"""

# another solution : "정규 표현식" 활용 풀이입니다..!!

import re

def string_split(s):
    s = s.lower()
    head= re.match('[\D]+',s)
    number = re.search('[\d]+',s)
    file = [head[0], int(number[0])]
    return file

def solution(files):
    answer = []
    new_files = []
    for i, file in enumerate(files):
        s_file = string_split(file.lower())
        s_file.append(i) # -->> "두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다."
        new_files.append(s_file)
    new_files.sort(key = lambda x : (x[0], x[1], x[-1])) # -->> "두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다."
    # answer = list(map(lambda x : files[x[-1]], new_files))
    for nf in new_files:
        answer.append(files[nf[2]])
        
    return answer

# 문제 총평 : "정규표현식"을 배제하고 푸니 너무 복잡했다..!!
