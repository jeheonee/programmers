def solution(board, moves):
    answer = 0
    stack = []
    for a in moves:
        for i in range(len(board)):
            if board[i][a-1] != 0:
                stack.append(board[i][a-1])
                board[i][a-1] = 0
                break
                
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:  
                stack = stack[:-2]
                answer += 2
    
    return answer