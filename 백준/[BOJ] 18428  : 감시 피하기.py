# <Q20> 감시 피하기 

# my solution

# my thoughts : 
# 1. 우선 "X"로 표시된 지점들의 위치를 모두 찾아서 리스트 하나를 생성하여 거기에 담아서 저장합시다..!!
# 2. 그리고 itertools 라이브러리의 조합 클래스 즉, combinations을 활용하여 장애물 3개를 설치할 수 있는 경우의 수를 모두 구합니다..!!
# 3. 2번을 통해 구한 모든 경우의 수를 다 checking 하면서 만약 모든 cases 중 하나의 경우 이상이 선생님의 감시를 피할 수 있으면 "YES"를 출력하고 그럴 수 없으면 "NO"를 출력하겠습니다..!!

from itertools import combinations

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input().split()))

# <step 1>
X_list = [] # <<-- 초기 그래프에서 "X"가 위치하는 지점들을 담을 리스트..!!
T_list = [] # <<-- 초기 그래프에서 "T"가 위치하는 즉, 선생님들이 위치해있는 지점들을 담을 리스트..!!
S_num = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            X_list.append((i, j))
            continue
        if graph[i][j] == "T":
            T_list.append((i, j))
            continue
        if graph[i][j] == "S":
            S_num += 1 # <<-- 입력으로 받은 n x n 복도에 있는 총 학생 수..!!
            continue

# <step 2>
O_cases = list(combinations(X_list, 3))

# <step 3>
def bfs(graph, start_v):
    up = 0
    down = 0
    left = 0
    right = 0

    while True: # 위쪽 탐색..!!
        up += 1
        new_v = (start_v[0], start_v[1] + up)
        if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1:
            if graph[new_v[0]][new_v[1]] == "O":
                break
            else:
                graph[new_v[0]][new_v[1]] = "T"
                continue
        else:
            break
    
    while True: # 아래쪽 탐색..!!
        down += 1
        new_v = (start_v[0], start_v[1] - down)
        if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1:
            if graph[new_v[0]][new_v[1]] == "O":
                break
            else:
                graph[new_v[0]][new_v[1]] = "T"
                continue
        else:
            break
    
    while True: # 왼쪽 탐색..!!
        left += 1
        new_v = (start_v[0] - left, start_v[1])
        if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1:
            if graph[new_v[0]][new_v[1]] == "O":
                break
            else:
                graph[new_v[0]][new_v[1]] = "T"
                continue
        else:
            break
    
    while True: # 오른쪽 탐색..!!
        right += 1
        new_v = (start_v[0] + right, start_v[1])
        if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1:
            if graph[new_v[0]][new_v[1]] == "O":
                break
            else:
                graph[new_v[0]][new_v[1]] = "T"
                continue
        else:
            break
    
    return graph

CheckFlag = False
for case in O_cases:
    (v1, v2, v3) = case
    copy_graph = [["X"] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            copy_graph[i][j] = graph[i][j]
    copy_graph[v1[0]][v1[1]] = "O"
    copy_graph[v2[0]][v2[1]] = "O"
    copy_graph[v3[0]][v3[1]] = "O"

    for start_v in T_list:
        copy_graph = bfs(copy_graph, start_v)

    s_count = 0
    for i in range(0, n):
        for j in range(0, n):
            if copy_graph[i][j] == "S": # <<-- 즉, 선생님이 탐색한 후에도 아직 학생이 살아있다면..!!
                s_count += 1
    
    if s_count == S_num: # <<-- 즉, 모든 학생이 살아있다면..!!
        CheckFlag = True
        break

if CheckFlag == False:
    print("NO")
else:
    print("YES")

# <A20> 감시 피하기
# 이 문제는 장애물을 정확히 3개 설치하는 모든 경우를 확인하여, 매 경우마다 모든 학생을 감시로부터 피하도록 할 수 있는지의 여부를 출력해야 한다.
# 그렇다면 장애물을 정확히 3개 설치하는 모든 경우의 수는 얼마나 될지 생각해보자.
# 복도의 크기는 N X N이며, N은 최대 6이다. 따라서 장애물을 정확히 3개 설치하는 모든 조합의 수는 최악의 경우 36C3이 될 것이다.
# 이는 10,000 이하의 수이므로 모든 조합을 고려하여 완전 탐색을 수행해도 시간 초과 없이 문제를 해결할 수 있다.
# 따라서 모든 조합을 찾기 위해서 DFS 혹은 BFS를 이용해 모든 조합을 반환하는 함수를 작성하거나, 파이썬의 조합 라이브러리를 이용할 수 있다.
# 또한 정확히 3개의 장애물이 설치된 모든 조합마다, 선생님들의 위치 좌표를 하나씩 확인하고 각각 선생님의 위치에서 상, 하, 좌, 우를 확인하여 학생이 한 명이라도 감시되는지를 확인해야 한다.
# 이는 별도의 watch() 메서드를 구현하면 편하다.
# 예를 들어 문제 설명에서 주어진 예시 그림을 보면 오른쪽과 같이 복도에 3개의 장애물이 설치되어 있다.
# 이때 각 선생님의 위치(T)에서 상, 하, 좌, 우의 위치를 확인하며 학생(S)이  존재하는지 확인해야 한다. 이는 반복문을 이용해 구현할 수 있으며,
# 답안 예시 소스코드에서는 watch() 메서드로 구현하였다. 예를 들어 (4, 2)의 위치에 있는 선생님이 감시하게 되는 위치는 오른쪽과 같을 것이다.
# 전체 소스코드는 다음과 같다. 답안 예시에서는 DFS/BFS를 직접 이용해 구현하지 않고, 파이썬의 조합 라이브러리를 이용하여 DFS/BFS를 대체하였다.

# A20.py
"""
# ....
# ....
# ....
# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations:
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = "O"
    # 학생이 한 명도 감지되지 않은 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")
"""
