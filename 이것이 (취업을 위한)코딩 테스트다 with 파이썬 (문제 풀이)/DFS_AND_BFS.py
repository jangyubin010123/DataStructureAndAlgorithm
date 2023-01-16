# 한 장으로 보는 알고리즘

# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 합니다.
# 자료구조 : "데이터를 표현하고 처리하는 방법"을 다룹니다.
# 스택 : 박스 쌓기에 비유할 수 있습니다. 흔히 박스는 아래에서부터 위로 차곡차곡 쌓습니다. 그리고 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 내려야 합니다.
# 이러한 구조를 선입후출(First In, Last Out)구조 또는 후입선출(Last In First Out)구조라고 합니다.

# 큐 : 대기 줄에 비유할 수 있습니다. 우리가 흔히 놀이공원에 입장하기 위해 줄을 설 때, 새치기하는 사람이 없으면 먼저 온 사람이 먼저 들어갑니다.
# 나중에 온 사람일수록 나중에 들어가기 때문에 흔히 '공정한' 자료구조라고 합니다. 이러한 구조를 선입선출(First In, First Out)구조라고 합니다.

# DFS : Depth-First Search, 즉 깊이 우선 탐색 알고리즘이며, 그래프를 탐색하는 알고리즘입니다.
# DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 스택 자료구조를 이용합니다.

# BFS : "너비 우선 탐색"이라는 의미입니다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘입니다.
# BFS는 선입선출 방식의 큐를 이용하면 효과적으로 구현할 수 있습니다.
# 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면, 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색합니다.

# <Q15> 특정 거리의 도시 찾기

# my solution
"""
from collections import deque

n, m, k, x = map(int, input().split())

graph = dict()

for _ in range(0, m):
    v1, v2 = map(int, input().split())
    if v1 not in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2) # <<-- 단방향 도로라고 문제의 조건에서 주어졌기 때문에 "graph[v2] = [v1]"처럼 역방향까지 고려할 필요는 없습니다..!!
# print(graph) # <<-- 인접 리스트(Adjacency List)기반 그래프를 생성해보았습니다..!!

def bfs(graph, start_v, visited):
    queue = deque()
    queue.append((start_v, 0))
    visited[start_v - 1] = True
    answer = [0] * n # <<-- start_v 로부터의 최단 거리 정보가 담길 1차원 리스트의 선언입니다..!!

    while queue:
        cur_v, depth = queue.popleft()

        if cur_v not in graph: # <<-- 단방향 도로이므로 이렇게 처리를 해줘야 합니다..!!
            continue # <<-- 해당 cur_v 정점에서는 다른 정점으로 뻗는 도로가 1개도 없는 상황이기 때문입니다..!!
        for v in graph[cur_v]:
            if v not in visited and answer[v-1] == 0:
                queue.append((v, depth + 1))
                answer[v - 1] = depth + 1
                visited[v - 1] = True
    
    return answer

count = 0
answer = []
answer = bfs(graph, start_v = x, visited = [False] * n)
print(answer) # <<-- 여기까지 ok..!!
for i, depth in enumerate(answer): # <<-- 즉, 인덱싱을 통한 for문을 이용하여 자동으로 오름차순 출력이 이루어지게 해줍니다..!!
    if depth == k:
        print((i+1), end = "\n")
        count += 1
if count == 0:
    print(-1) # <<-- 문제의 조건 中 "이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력합니다."
"""

# <A15> 특정 거리의 도시 찾기
# -->> "문제에서 모든 도로의 거리는 1이다."
# -->> "이는 다시 말해 모든 간선의 비용이 1이라는 의미인데," -->> "그래프에서 모든 간선의 비용이 동일할 때는 너비 우선 탐색(BFS)을 이용하여 최단 거리를 찾을 수 있다."
# -->> """다시 말해 "모든 도로의 거리는 1이라는 조건 덕분에 너비 우선 탐색을 이용하여 간단히 해결"할 수 있는 것이다."""
# 문제의 조건을 살펴보면 노드의 개수 N은 최대 300,000개이며 간선의 수 M은 최대 1,000,000개이다.
# 따라서 이 문제는 너비 우선 탐색을 이용하여 시간 복잡도 O(N + M)으로 동작하는 소스 코드를 작성하여 시간 초과 없이 해결할 수 있다.
# 먼저 특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 뒤에,
# 각 최단 거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 출력하면 된다.

# A15.py 답안 예시
"""
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i, end = "\n")
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1을 출력
if check == False:
    print(-1, end = "\n")
"""

# <Q16> 연구소

# my solution
# 1. 새로 세울 수 있는 벽 3개를 0이 있는 위치에 임의로 세운다. <<-- 즉, 모든 경우의 수를 고려해야 한다..!!
# 2. 임의의 위치에 벽 3개를 세운 후 "2"의 값을 가지는 지점에서 BFS/DFS를 실행한 후 바이러스가 퍼진 영역(즉, 2로 바뀐 영역)을 counting 한 후 전체 지도의 크기에서 뺀다.
# 3. 모든 경우에서 2번을 수행 후 최댓값을 출력한다..!!
"""
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
                graph[new_v[0]][new_v[1]] = 2 # <<-- 새롭게 감염된 지역을 2으로 바꿔줍시다..!! (-->> 즉, 0에서 2로..!!)


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

zero_list = []
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

for v1, v2, v3 in cases:
    count = 0
    copy_graph = [[0] * m for i in range(n)]
    # copy_graph = graph # <<-- 여기가 잘못된 듯..!! <<-- "즉, 파이썬에서는 변수가 포인터 변수의 역할을 하기 때문입니다..!!"
    # print(copy_graph)
    for i in range(0, n):
        for j in range(0, m):
            copy_graph[i][j] = graph[i][j]
    copy_graph[v1[0]][v1[1]] = 1
    copy_graph[v2[0]][v2[1]] = 1
    copy_graph[v3[0]][v3[1]] = 1 # <<-- 즉, 3개의 벽을 세워줍시다..!!
    for x, y in two_list:
        bfs(copy_graph, (x, y))
    for i in range(0, n):
        for j in range(0, m):
            if copy_graph[i][j] == 0:
                count += 1
    answer.append(count)

print(max(answer))
"""

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

# <A17> 경쟁적 전염
# 이 문제는 너비 우선 탐색(BFS)를 이용하여 해결할 수 있다. 다만, 문제에 나와 있는 대로 각 바이러스가 낮은 번호부터 증식한다는 점을 기억하자.
# -->> "낮은 번호부터 증식하므로, 초기에 큐(Queue)에 원소를 삽입할 때는 낮은 바이러스의 번호부터 삽입해야 한다."
# -->> "이후에 너비 우선 탐색을 수행하여 방문하지 않은 위치를 차례대로 방문하도록 하면 된다."

# 답안 예시
"""
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스 에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호부터 바이러스가 먼저 증식하므로)
data.sort(key = lambda x : x[0]) # <<-- 여기서 사실 data.sort() 라고 써도 됩니다. 어차피 정렬시 처음 기준은 첫 번째 원소로 자동으로 비교되기 때문입니다..!!
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복..!!
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
"""
