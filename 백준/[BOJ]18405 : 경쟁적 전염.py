# <Q17> 경쟁적 전염
# 문제 설명 : 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식하는데, -->> "매초 번호가 낮은 종류의 바이러스부터 먼저 증식합니다."
# 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없습니다..!!
# .... 이때 X 와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1, 1)에 해당합니다.

# my solution
# 참고> 여러 변수 사용시 "중복된 이름"을 조심할 것..!!

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]
for i in range(0, n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip().split()))
s, result_x, result_y = map(int, input().split())
# print(x, y)
# print(graph) <<-- ok..!! 그래프 생성까진 완료..!!
d = dict() # <<-- 1부터 K까지 각 바이러스가 위치하는 지점을 담기 위한 딕셔너리 자료형의 선언입니다..!!
for i in range(1, k + 1):
    d[i] = list()
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] != 0:
            d[graph[i][j]].append((i, j))
time = 0
while time < s:
    time += 1
    for i in range(1, k + 1):
        next_list = []
        while len(d[i]) != 0:
            x,y = d[i].pop(0)
            # print(x, y)
            for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx = x + dir[0]
                ny = y + dir[1]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                    if graph[nx][ny] == 0:
                        next_list.append((nx, ny)) # <<-- 도대체 이게 왜 틀린거임 어이가 없네..!!
                        graph[nx][ny] = i
        d[i] = next_list

# print(graph) # <<-- 여기까지 ok..!!
# print(graph[2][1])
print(graph[result_x - 1][result_y - 1])



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
