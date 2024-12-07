board = [
    [0,-1,1],
    [-1,1,0],
    [1,0,0],
]

def win_checker(board: list) -> int:
    # check rows
    for row in board:
        row_sum = sum(row)
        if row_sum == 3:
            return 1
        elif row_sum == -3:
            return -1
        
    # check columns
    for column_index in range(0,3): #slicing?
        column_sum = 0
        for row_index in range(0,3):
            value = board[row_index][column_index]
            column_sum += value
        if column_sum == 3:
            return 1
        elif column_sum == -3:
            return -1

    # check descending diagonal
    diag_sum = 0
    for index in range(0,3):
        diag_sum += board[index][index]
    if diag_sum == 3:
            return 1
    elif diag_sum == -3:
            return -1
            
    # check ascending diagonal
    for index in range(0,3):
         # this is my boolean version rather than eric's mathmatical version
         if board[2][0] and board[1][1] and board[0][2] == 1:
              return 1
         elif board[2][0] and board[1][1] and board[0][2] == -1:
              return -1
    return 0

print(win_checker(board))