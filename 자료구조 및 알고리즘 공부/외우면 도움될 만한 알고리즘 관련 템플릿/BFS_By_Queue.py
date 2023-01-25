from collections import deque

# BFS 메서드 예제
def bfs(graph, start_v, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start_v])
    # 현재 노드를 방문 처리
    visited[start_v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        cur_v = queue.popleft()
        print(cur_v, end = " ")
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for v in graph[cur_v]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# 참고> 이러한 그래프 표현 방식을 인접 리스트 기반의 그래프 표현 방식이라고 부르곤 합니다..!!
graph = [
    [],
    [2, 3 ,8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
