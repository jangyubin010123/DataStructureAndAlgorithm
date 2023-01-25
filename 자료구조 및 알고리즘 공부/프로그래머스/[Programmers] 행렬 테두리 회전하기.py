# my solution1

def Rotation(q, arr): # <<-- 각 테두리에 해당하는 모든 위치를 구해서 리스트 슬라이싱을 이용해서 값 변경을 해줍시다..!!
    copy_arr = [[0] * len(arr[0]) for _ in range(len(arr))]
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            copy_arr[i][j] = arr[i][j] # 시계방향으로 한 칸 회전하기전 arr 배열 카피본 생성..!!
    garo = q[3] - q[1] + 1 # 가로 길이
    sero = q[2] - q[0] + 1 # 세로 길이
    # print(garo, sero)
    x = q[0]
    y = q[1]
    Points = list() # 테두리에 해당하는 지점(위치)들을 담을 리스트의 선언입니다..!!
    for _ in range(1, garo):
        Points.append((x-1, y-1))
        y += 1

    # print(Points)

    for _ in range(1, sero):
        Points.append((x-1, y-1))
        # print(Points)
        x += 1
        
    for _ in range(1, garo):
        Points.append((x-1, y-1))
        y -= 1
        
    for _ in range(1, sero):
        Points.append((x-1, y-1))
        x -= 1
    # <<-- 즉, 여기까지 수행하면 테두리에 해당하는 지점(위치)들을 다 담은 것입니다..!!
    
    After = Points[1::1] + Points[0:1:1] # 시계방향 회전하기 전의 지점들의 값이 시계 방향 회전 후 가야되는 위치들을 담은 리스트라고 보시면 됩니다..!!
    
    min_value = arr[Points[0][0]][Points[0][1]]
    for new_v, v in list(zip(After, Points)):
        arr[new_v[0]][new_v[1]] = copy_arr[v[0]][v[1]]
        if arr[new_v[0]][new_v[1]] < min_value:
            min_value = arr[new_v[0]][new_v[1]]
    
    return min_value
    
    
            

def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(0, rows)]
    v = 1
    for i in range(0, rows):
        for j in range(0, columns):
            arr[i][j] = v
            v += 1
    for q in queries:
        answer.append(Rotation(q, arr))
    # print(Rotation([2,2,5,4], arr))        
    return answer


print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
