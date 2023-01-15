# my solution

from collections import deque

# BFS 메서드 정의
def bfs(graph, start_v):
    m = len(graph) # <<-- 세로 길이가 됨..!!
    n = len(graph[0]) # <<-- 가로 길이가 됨..!!
    direction = [(0,1), (0,-1), (-1,0), (1,0)] # <<-- 문제의 조건 중에서 상, 하, 좌, 우로 이동할 수 있다고 하였기 때문입니다..!!
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(start_v)
    # 큐가 빌 때까지 반복
    while queue:
        cur_v = queue.popleft()
        for d in direction:
            new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
            if 0 <= new_v[0] <= m-1 and 0 <= new_v[1] <= n-1:
                if graph[new_v[0]][new_v[1]] == 1: # <<-- 즉, 아직 방문하지 않은 정점이라면..!!
                    queue.append(new_v) # <-- 큐(Queue)에 정점이 들어간다는 것은 방문할 예정이라는 것입니다..!!
                    graph[new_v[0]][new_v[1]] = graph[cur_v[0]][cur_v[1]] + 1
    
def solution(maps):
    bfs(maps, start_v = (0,0))
    print(maps)
    m = len(maps)
    n = len(maps[0])
    if maps[m-1][n-1] == 1:
        return -1
    else:
        return maps[m-1][n-1]
