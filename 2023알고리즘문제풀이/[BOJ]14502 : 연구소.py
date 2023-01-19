# <Q16> 연구소

# my solution
# 1. 새로 세울 수 있는 벽 3개를 0이 있는 위치에 임의로 세운다. <<-- 즉, 모든 경우의 수를 고려해야 한다..!!
# 2. 임의의 위치에 벽 3개를 세운 후 "2"의 값을 같는 지점에서 BFS/DFS를 실행한 후 바이러스가 퍼진 영역(즉, 2로 바뀐 영역)을 counting 한 후 전체 지도의 크기에서 뺀다.
# 3. 모든 경우에서 2번을 수행 후 최댓값을 출력한다..!!

from itertools import combinations

from collections import deque

def bfs(graph, start_v):
    queue = deque()
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()
        
        for d in [(0,1), (0,-1), (-1,0), (1,0)]:
            new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
            if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= m-1 and graph[new_v[0]][new_v[1]] == 0:
                queue.append(new_v)
                graph[new_v[0]][new_v[1]] = 2 # <<-- 2를 통해 감염된 지역을 2으로 바꿔줍시다..!! -->> 즉, 0에서 2로..!!


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

# print(graph) # <<-- 여기까지 ok..!!

zero_list = []

# <A16> 연구소
# 이 문제는 벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다. 간단하게 생각해보면 전체 맵의 크기가 8 X 8이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우(바이러스가 하나도 존재하지 않은 경우) 64C3이 될 것이다.
# 이는 100,000보다 작은 수이므로, 모든 경우의 수를 고려해도 제한 시간 안에 문제를 해결할 수 있다는 것을 알 수 있다.
# 또한 모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 이용하거나, DFS 혹은 BFS를 이용하여 해결할 수 있다. 따라서 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산하면 된다.
# 안전 영역의 크기를 구하는 것 또한 DFS 와 BFS를 이용하여 계산할 수 있다.
# 결과적으로 여기서는 가능한 모든 경우의 수를 계산하되, 안전 영역을 계산할 때 DFS나 BFS를 적절히 이용해야 한다는 점이 특징이다.
# 따라서 DFS 혹은 BFS를 사용하여 완전 탐색을 수행해야 한다는 점에서 DFS/BFS문제 혹은 완전 탐색 문제로 분류할 수 있다.
# 또한 구현 과정이 까다롭기 때문에 구현 유형으로 분류할 수도 있다.
# 문제 풀이 아이디어를 간략히 설명하면, 초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치하는 것이다.
# 매번 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 계산하여 안전 영역을 구해야 한다.
# 문제에서 제시되었던 예시를 확인해보자.
# ....

# A16.py 답안 예시
# ....

# <Q17> 경쟁적 전염
# 문제 설명 : 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식하는데, -->> "매초 번호가 낮은 종류의 바이러스부터 먼저 증식합니다."
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없습니다..!!
# .... 이때 X 와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1, 1)에 해당합니다.

# my solution
"""
from collections import deque

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(0, n):
    graph[i] = list(map(int, input().split()))
s, x, y = map(int, input().split())

# 음, 일단 초기에 1~k의 바이러스가 어느 위치에 있는지 확인해볼까..??
v_dict = dict()

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            if graph[i][j] not in v_dict:
                v_dict[graph[i][j]] = [(i, j)]
            else:
                v_dict[graph[i][j]].append((i, j))

# print(v_dict) # <<-- 출력 결과 Ex : {1: [(0, 0)], 2: [(0, 2)], 3: [(2, 0)]}

for time in range(0, s): # <<-- 즉 1초 경과마다..!!
    for i in range(1, k + 1): # <<-- 모든 바이러스의 종류를 1칸 씩 퍼트리면서 (물론, 가능하다면..!!)
        i_list = [] # <<-- 다음 1초 때 체킹할 정점들을 담을 임시 리스트의 선언이라고 보시면 됩니다..!!
        while v_dict[i]:
            cur_v = v_dict[i].pop(0)
            for d in [(0,1), (0,-1), (-1,0), (1,0)]:
                new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
                if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1 and graph[new_v[0]][new_v[1]] == 0:
                    i_list.append(new_v)
                    graph[new_v[0]][new_v[1]] = i
        v_dict[i] = i_list

print(graph)
print(graph[x-1][y-1])
"""
two_list = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            two_list.append((i, j))
            continue

        if graph[i][j] == 0:
            zero_list.append((i, j)) # <<-- 즉, 135 ~ 138행을 통해 벽을 세울 수 있는 위치를 임시로 저장해 둡니다..!!
# print(list(combinations(zero_list, 3))) # <<-- 0인 지점들 중에서 순서를 고려하지 않고 3개씩 뽑았을 때 나올 수 있는 경우의 수입니다..!!

cases = list(combinations(zero_list, 3))
answer = []

# print(cases)
# print(two_list)

for v1, v2, v3 in cases:
    count = 0
    copy_graph = [[0] * m for i in range(n)]
    # copy_graph = graph # <<-- 여기가 잘못된 듯..!! <<-- 즉, 파이썬에서는 변수가 포인터 변수의 역할을 하기 때문입니다..!!
    # print(copy_graph)
    for i in range(0, n):
        for j in range(0, m):
            copy_graph[i][j] = graph[i][j]
    copy_graph[v1[0]][v1[1]] = 1
    copy_graph[v2[0]][v2[1]] = 1
    copy_graph[v3[0]][v3[1]] = 1 # <<-- 즉, 3개의 벽을 세워줍시다..!!
    # print(copy_graph)
    for x, y in two_list:
        bfs(copy_graph, (x, y))
        # print(copy_graph)
    for i in range(0, n):
        for j in range(0, m):
            if copy_graph[i][j] == 0:
                count += 1
    answer.append(count)

print(max(answer))
