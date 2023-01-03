# my solution
def solution(board, moves):
    answer = 0
    stack = [] # 크레인으로 뽑은 인형을 저장하는 바구니
    # 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다.
    # 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다.
    TopIndexs = [0] * len(board[0]) # 각 열마다 인형이 존재하는 가장 높은 위치를 기록하는 리스트의 선언..!!
    # 초깃값으로 0을 넣어주어서 꽉 차있다고 가정하고 진행..!!
    for move in moves:
        while board[TopIndexs[move - 1]][move - 1] == 0 and TopIndexs[move - 1] < len(board[0]) - 1:
            TopIndexs[move - 1] += 1
        
        if board[TopIndexs[move - 1]][move - 1] == 0 and TopIndexs[move - 1] == len(board[0]) - 1: # 즉, 맨 아래에 도달했는데도 인형이 아예 없는 경우..!!
            continue
        temp = board[TopIndexs[move - 1]][move - 1]
        board[TopIndexs[move - 1]][move - 1] = 0 # 인형을 뽑은 후에는 숫자를 0으로 바꿔주어 표시를 남겨주자..!!
        stack.append(temp) # 크레인으로 해당 인형을 뽑아 바구니에 넣는다..!!
        if len(stack) <= 1:
            continue # 바구니에 1개 이하의 인형이 있을 때는 아무 일도 일어나지 않습니다..!!
        else:
            if stack[-1] == stack[-2]: # 즉, 바구니에 있는 맨 위의 두개의 인형이 같은 경우..!!
                stack.pop()
                stack.pop()
                answer += 2
    return answer

# another solution
"""
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
"""
