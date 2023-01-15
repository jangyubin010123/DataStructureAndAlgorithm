# my solution

def dfs(graph, start_v, visited): # <<-- 재귀함수를 이용한 dfs함수의 구현입니다..!!
    visited.append(start_v)
    
    for v in graph[start_v]:
        if v not in visited:
            dfs(graph, v, visited)
    
    return visited

def solution(n, computers):
    answer = 0
    graph = {} # <<-- 인접 리스트(Adjacency List) 기반으로 그래프를 (재)표현해 봅시다..!!
    # 적어도 나한테는 인접 행렬 기반 그래프로 푸는 것보단 인접 리스트 기반 그래프를 이용해서 푸는 게 더 잘 풀리는 것 같아서 난 이렇게 함..!!
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i == j: # <<-- 즉, 자기 자신일 때는 Counting을 제외 시켜야 하기 때문입니다..!!
                continue
            if computers[i][j] == 1: # <<-- 즉, 직접적으로 연결되어있는 경우라면..!!
                if i not in graph:
                    graph[i] = [j]
                else:
                    graph[i].append(j)
    # print(graph) <<-- 이로써 인접 리스트(adjacency list)기반의 그래프를 생성해보았습니다..!!
    # 이제 DFS/BFS를 이용하여 문제를 해결해봅시다..!!
    total_visited = []
    count = 0
    for k in graph.keys():
        visited = []
        visited = dfs(graph, k, visited)
        visited = set(visited) # <<-- 순서가 다를 경우 다르게 counting 되는 것을 막기 위함입니다..!!
        if visited not in total_visited:
            total_visited.append(visited)
            count += len(visited)
        else:
            continue
    answer = len(total_visited) + (n - count)
    # * len(total_visited) : 여러 정점들로 구성된 네트워킹의 갯수
    # * (n - count) : 한 정점으로만 구성된 네트워킹의 갯수
    return answer
