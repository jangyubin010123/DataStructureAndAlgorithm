# my solution2 : "시간초과"를 해결한 solution입니다..!!

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(start_v):
    united = []
    united.append(start_v)
    visited[start_v[0]][start_v[1]] = True
    queue = deque()
    queue.append(start_v)

    while queue:
        cur_v = queue.popleft()
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_v = (cur_v[0] + d[0], cur_v[1] + d[1])
            if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1:
                if visited[new_v[0]][new_v[1]] == False:
                    if l <= abs(graph[new_v[0]][new_v[1]] - graph[cur_v[0]][cur_v[1]]) <= r:
                        united.append(new_v)
                        visited[new_v[0]][new_v[1]] = True
                        queue.append(new_v)
    return united

count = 0
while True:
    checkFlag = False
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                united = []
                united = bfs((i,j))
                if len(united) == 1:
                    continue
                else:
                    checkFlag = True
                    sum = 0
                    num = len(united)
                    for x, y in united:
                        sum += graph[x][y]
                    new_value = sum // num
                    for x, y in united:
                        graph[x][y] = new_value
    if checkFlag == False: # <<-- 즉, 길이가 1인 united만 나타난다면 더 이상 인구수 이동이 불필요한 상황이므로 이때는 while문을 탈출시켜서 값을 출력하도록 해줘야 합니다..!!
        break
    else:
        count += 1
        continue

print(count)
