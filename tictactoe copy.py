board = [
    [-1,1,1],
    [0,-1,0],
    [1,0,-1],
]
# trying to do this with booleans instead of sums like eric's example was
# thoughts: could check for row contents in separate functions and call them in win_checker? I want a way to check which row is fucking this up lol because it's telling me i'm getting a row win for 1 when that's not actually the case
def win_checker(board: list) -> int:
    for index in range(0,3):
        # if (row1) or (row2) or (row3)
        if (board[0][0] and board[0][1] and board[0][2]) or (board[1][0] and board[1][1] and board[1][2]) or (board[2][0] and board[2][1] and board[2][2]) == 1:
            print("row win")
            return 1
        elif (board[0][0] and board[0][1] and board[0][2]) or (board[1][0] and board[1][1] and board[1][2]) or (board[2][0] and board[2][1] and board[2][2]) == -1:
            print("row win")            
            return -1
        
        # if (column1) or (column2) or (column3)
        if (board[0][0] and board[1][0] and board[2][0]) or (board[0][1] and board[1][1] and board[2][1]) or (board[0][2] and board[1][2] and board[2][2]) == 1:
            print("column win")
            return 1
        if (board[0][0] and board[1][0] and board[2][0]) or (board[0][1] and board[1][1] and board[2][1]) or (board[0][2] and board[1][2] and board[2][2]) == -1:
            print("column win")
            return -1
        
        # descending diagonal
        if board[0][0] and board[1][1] and board[2][2] == 1:
              print("descending diagonal win")
              return 1
        elif board[0][0] and board[1][1] and board[2][2] == -1:
              print("descending diagonal win")
              return -1

        # ascending diagonal
        if board[2][0] and board[1][1] and board[0][2] == 1:
              print("ascending diagonal win")
              return 1
        elif board[2][0] and board[1][1] and board[0][2] == -1:
              print("ascending diagonal win")
              return -1
        
    return 0

print(win_checker(board))