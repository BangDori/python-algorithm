def solution(board, moves):
    answer = 0
    
    new_board = [[0 for _ in range(len(board))] for _ in range(len(board))]
    
    for row in range(len(board)):
        for col in range(len(board)):
            new_board[col][row] = board[row][col]

    output_list = []
    new_board = [[idx for idx in row if idx != 0] for row in new_board]
        
    for move in moves:
        if len(new_board[move-1]) == 0:
            continue

        output = new_board[move-1].pop(0)
        print(move, output)
        
        if output == 0:
            continue
            
        output_list.append(output)
                
        if len(output_list) >= 2:
            if output_list[-1] == output_list[-2]:
                answer += 2
                output_list.pop(); output_list.pop()
                continue
                
    return answer