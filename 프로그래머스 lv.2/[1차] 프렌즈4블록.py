# my solution

def pop_blocks(new_board, n, m):
    # <step 2> 이제, .... 좌상단의 블록을 기준으로 2 x 2 블록이 터질 수 있는지 없는지 조사해야 합니다..!!
    count = 0
    pop_set = set() # <<-- 터지는 블록의 인덱스를 담을 집합 자료형 pop_set의 선언입니다..!!
    # <<-- 중복되는 인덱스가 카운팅되는 것을 방지하기 위해 집합 자료형으로 선언하였습니다..!!
    for i in range(0, n-1):
        for j in range(0, m-1):
            if new_board[i][j] == new_board[i][j+1] == new_board[i+1][j] == new_board[i+1][j+1] != "@": # 참고 > 여기서 "@" 문자가 의미하는 것은 카카오프렌즈 블록이 없는 자리 즉, 밑에 있는 블록이 터져서 해당 자리가 비워진 것을 의미합니다..!!
                pop_set.update(((i,j), (i,j+1), (i+1,j), (i+1,j+1)))
    # <step 3> 터져야 할 블록들을 임시로 문자 "0"으로 잠시 교체해줍니다. 
    # <step 4> 그리고 "0"의 갯수만큼 "@"을 만들어서 상단에 채워줍니다..!!
    pop_list = list(pop_set) # <<-- for문을 돌기 위해서 잠시 리스트 형태로 바꿔줍시다..!!
    for i, j in pop_list: # <<-- Actually, 사실 집합 자료형으로도 for문을 돌 수 있습니다..!!
        new_board[i][j] = "0"
        count += 1
    for i in range(0,n):
        count_of_0 = new_board[i].count("0")
        popped = ["@"] * count_of_0
        new_board[i] = popped + [b for b in new_board[i] if b != "0"]
    
    return count
    
def solution(m, n, board):
    answer = 0
    
    # <step 1> 일단 행/열을 조작하기 쉽게 하기 위해 board를 변환해주자..!!
    # print(list(zip(*board)))
    # 출력 결과 Ex : 	[('T', 'R', 'R', 'T', 'T', 'T'), ('T', 'R', 'R', 'R', 'T', 'M'), ('T', 'F', 'R', 'R', 'M', 'M'), ('A', 'A', 'F', 'R', 'M', 'T'), ('N', 'C', 'C', 'A', 'M', 'T'), ('T', 'C', 'C', 'A', 'F', 'J')]
    new_board = []
    for b in list(map(list, zip(*board))):
        new_board.append(b)
    # print(new_board) <<-- 여기까지 ok..!!
    # 출력 결과 Ex : ['TRRTTT', 'TRRRTM', 'TFRRMM', 'AAFRMT', 'NCCAMT', 'TCCAFJ']
    # 즉, 기존의 배열은 블록이 빈자리를 채우는 과정에서 떨어지는 방향이 북쪽에서 남쪽으로 떨어지는 방향이었다면, 변환된 배열은 서쪽에서 남쪽으로 떨어질 것입니다..!!
    
    # <step 2~4>를 마친 후 터져야할 블록의 갯수가 0개가 아닐 때 까지 해당 수행들을 반복해주면 됩니다.!!
    while True:
        count = pop_blocks(new_board, n, m)
        if count == 0:
            break
        else:
            answer += count
            
    return answer

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))


# another solution : 풀이 참조 출처 : "https://velog.io/@tjdud0123/%ED%94%84%EB%A0%8C%EC%A6%88-4%EB%B8%94%EB%A1%9D-2018-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python"

# 솔루션 #
# board를 행/열을 바꾸어 조작하기 쉽게 만든다.
# 아래 오른쪽 점을 기준으로 board를 순회하면서 4칸이 같은 블록을 찾아(공백 제외) pop_set에 넣어준다. 중복되는 블록이 두번 계산되지 않게 하기위해 set을 사용한다. 터진 좌표를 0으로 만들어주고 없어진 개수만큼 "_"(empty)블록을 위에 위치시킨 후 나머지 블록(0이 아닌 블록)들을 모아준다.
# 터진 갯수를 반환하여 count에 더해준다.

# -->> "터지는 블록 갯수가 0일 때까지 반복한다."

# 코드

# 파이썬
"""
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n): # <<-- 즉, 2 x 2 정사각형 중 오른쪽 아래 블록을 기준으로 잡고 순회하겠다는 뜻입니다..!!
        for j in range(1, m):
            if b[i][j] == b[i][j-1] == b[i-1][j] == b[i-1][j-1] != "_":
                pop_set.update(set([(i,j), (i,j-1), (i-1,j), (i-1,j-1)]))
    # 이제 터진 블록을 숫자 0으로 대체한 후 -->> 남은 블록들을 모아주는 작업을 해야합니다..!!
    for (i, j) in pop_set:
        b[i][j] = 0
    for i in range(0,len(b)):
        empty = ["_"] * b[i].count(0)
        b[i] = empty + [block for block in b[i] if block != 0]
        # 참고 > 리스트들끼리는 더하기(+)연산으로 둘을 합칠 수 있습니다..!!
        # -->> 블록들이 터지고 난 후 위에 있는 블록들은 동쪽으로 이동해야 하기 때문입니다..!!
    
    return len(pop_set)

def solution(m, n, board):
    answer = 0
    changed_board = list(map(list, zip(*board))) # 참고 > 이 30행으로 인하여 블록이 떨어지는 방향이 -->> "북->남 방향이 서->동 방향으로 바뀝니다..!!"
    # print(b)
    # board를 행/열을 바꾸어 조작하기 쉽게 만든다.
    # 기존 board는 블록이 터지고 나서 위에 있는 블록이 떨어지는 방향이 북쪽에서 남쪽이었다면 board를 행/열을 바꾸어 조작하기 쉽게 만든 b는 블록이 터직 나서 위에 있는 블록이 떨어지는 방향이 서쪽에서 동쪽이다..!!
    while True:
        nums = pop_num(changed_board, m, n)
        if nums == 0: return answer
        answer += nums
"""

# another solution2
"""
def solution(m, n, board):
    x = board
    x2 =[]

    for i in x: 
        x1 = []
        for i2 in i:
            x1.append(i2)
        x2.append(x1)
    
    point = 1
    while point != 0:
        list = []
        point = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != '팡!':
                    list.append([i, j])
                    point += 1

        for i2 in list:
            i, j = i2[0], i2[1]
            x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = '팡!', '팡!', '팡!', '팡!'

        for i3 in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if x2[i + 1][j] == '팡!':
                        x2[i + 1][j], x2[i][j] = x2[i][j], '팡!'

    cnt = 0
    for i in x2:
        cnt += i.count('팡!')
    return cnt
"""
