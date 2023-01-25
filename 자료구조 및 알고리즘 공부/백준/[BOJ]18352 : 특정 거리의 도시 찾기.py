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
# 참고> 백준에서 이전에 오답처리 받은 이유는 데이터를 입력받을 때 input()을 사용하였기 때문에 sys모듈을 사용했을 때보다 시간이 많이 걸려서 시간초과 판정을 받은 것 같습니다..!!

from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
# print(graph) # <<-- 즉, 입력을 통해 받은 단방향 간선들의 정보들을 참고해서 인접 리스트 기반 그래프를 형성하였습니다..!!
# 출력 결과 Ex : {1: [2, 3], 2: [3, 4], 3: [], 4: []}

distance = [0] * (n + 1) # 시작점이 X인 도시에서부터 각각의 도시 간에 최단 거리를 등록할 리스트의 선언입니다..!!

def bfs(graph, start_v, distance):
    distance[start_v] = 0
    queue = deque()
    queue.append((start_v, 0))

    while queue:
        cur_v, depth = queue.popleft()

        for v in graph[cur_v]:
            if distance[v] == 0:
                queue.append((v, depth + 1))
                distance[v] = depth + 1

bfs(graph, x, distance)

count = 0
for i in range(1, n + 1):
    if i == x:
        continue
    if distance[i] == k:
        print(i)
        count += 1

if count == 0:
    print(-1)  

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
    print(-1)
