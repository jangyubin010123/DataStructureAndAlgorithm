# 그래프 (Graph)

# Graph
# 그래프 정의
# -->> 그래프 G(V,E)는 어떤 자료나 개념을 포함하는 정점들(vertex)들의 집합 V와 이들을 연결하는 간선(edge)들의 집합 E로 구성된 자료구조입니다.
# 참고> 모든 트리는 그래프라고 불릴 수 있지만, 그 역은 성립하지 않는다..!!

# 그래프 종류
# 1. 방향 그래프 vs. "무(방)향 그래프"(코테에 가장 많이 등장.)
# 2. 다중 그래프 vs. "단순 그래프"
# 3. "가중치 그래프" -->> 다익스트라

# 그래프 활용
# 현실 세계의 사물이나 추상적인 개념간의 연결 관계를 표현한다.
# 그래프는 현실의 문제를 해결하기 위한 도구로써 유용하게 이용이 된다. -->> 문제가 많이 나온다.
# * 도시들을 연결하는 도로망 : 도시(vertex), 도로망(edge)
# * 지하철 연결 노선도 : 정거장(vertex), 정거장을 연결하는 선(edge)
# * ....
# * 소셜 네트워크 분석 : 페이스북의 계정(vertex), follow 관계(edge)

# Graph 표현 방법
# 인접 리스트(adjacency list)
# 인접 행렬(adjacency matrix)
# 암시적 그래프(implicit graph)

# 인접 행렬(adjacency matrix)
"""
graph = [
    [0,0,1,0,1],
    [0,0,0,1,1],
    [1,0,0,0,1],
    [0,1,0,0,1],
    [1,1,1,1,0]
]
"""
# But, 그래프를 나타내는 데 있어서 (즉, 코딩테스트에서는) 인접 행렬(adjacency)은 자주 쓰이는 기법이 아닙니다..!!
# why?> 메모리 낭비가 심하다. 즉, 비효율적이다..!!

# 인접 리스트(adjacency list)
"""
graph = {
    1 : [3,5],
    2 : [4,5],
    3 : [1,5],
    4 : [2,5],
    5 : [1,2,3,4]
}
"""
# 암시적 그래프(implicit graph) : 사실상 코테에서 가장 많이 쓰이는 기법입니다..!!
# (ex) 벽 : 1 , 벽x : 0
"""
graph = [
    [1,1,1,1,1],
    [0,0,0,1,1],
    [1,1,0,1,1],
    [1,0,0,0,0],
    [1,1,1,1,1]
]
"""
# 그래프 순회 Traversal

# 그래프 순회 Graph Traversal
# -->> 그래프 순회란 그래프 탐색(Search)라고도 불리우며, 그래프의 각 정점을 방문하는 과정을 말한다. 그래프
# 순회에는 크게 깊이 우선 탐색(Depth-First Search)과 너비 우선 탐색(Breadth-First Search)의 2가지
# 알고리즘이 있다.

# 너비 우선 탐색
# Breadth-first Search
# BFS
"""
graph = { # 인접 리스트(adjacency list)기반의 그래프 표현 방식입니다..!!
    'A': ['B','D','E'],
    'B': ['A','C','D'],
    'C': ['B'],
    'D': ['A','B'],
    'E': ['A']
}
"""
"""
from collections import deque
# '템플릿'처럼 딸딸 외워야 한다..!!
def bfs(graph, start_v):
    visited = [] # 방문했던 노드 목록을 차례대로 저장할 리스트와
    queue = deque() # 다음으로 방문할 노드의 목록을 차례대로 저장할 덱 자료구조(큐)를 만들어주자.

    queue.append(start_v) # 우선 맨 처음에는 당연히 시작 노드를 큐에 넣어준다.

    while queue: # 큐의 목록이 바닥날때까지(더 이상 방문할 노드가 없을 때까지) loop를 돌려준다.
        cur_v = queue.popleft() 
        if cur_v not in visited: # 해당 노드가 아직 방문 리스트에 없다면,
            visited.append(cur_v) # 방문 리스트에 추가해주고,
            for v in graph[cur_v]: # 해당 노드의 자식 노드들을 큐에 추가해준다.
                queue.append(v)
        else: 
            continue
    return visited

print(bfs(graph,'A'))
"""

# 깊이 우선 탐색
# Depth-first search

# 내가 짜본 dfs 코드..!!
"""
visited = []
def dfs(graph, cur_v):
    if cur_v in visited:
        return
    visited.append(cur_v)
    for v in graph[cur_v]:
        dfs(graph,v)

dfs(graph,'C')
print(visited)
"""

# 개발남노씨님`s 코드
graph = { # 인접 리스트(adjacency list)기반의 그래프 표현 방식입니다..!!
    'A': ['B','D','E'],
    'B': ['A','C','D'],
    'C': ['B'],
    'D': ['A','B'],
    'E': ['A']
}
visited = []

def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)

dfs('A')
# print(visited)

"""
# 내가 짜본 또다른 dfs 코드..!!
visited = []

def dfs(cur_v):
    if cur_v not in visited:
        visited.append(cur_v)
        for v in graph[cur_v]:
            dfs(v)
    else:
        return

dfs('A')
print(visited)
"""

