def empty_board(rows = 10, columns = 10):
    board = [[" ~ " for j in range(columns)] for i in range(rows)]
    return board

def print_final_empty_board(board):
    print("   A  B  C  D  E  F  G  H  I  J")
    for i in range(len(board)):
        row_number = i + 1
        row = board[i]
        print(f"{row_number:2}" + "".join(row)) 
        
if __name__ == "__main__":
    battleship_board = empty_board()
    print_final_empty_board(battleship_board)
 



   