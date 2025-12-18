BOARD_SIZE = 10

def shot(board, row, column):

    if board[row][column] == " ~ ":
        board[row][column] = " x "
        return "miss"

    if board[row][column] == " x ":
        return "already hit"

    if board[row][column] == " ■ ":
        board[row][column] = " ■ " 
        if destroyed(board, row, column):
            mark_destroyed(board, row, column)
            return "destroyed"
        return "hit"
    return "miss"


def destroyed(board, row, column):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     #left, right, down, up

    for change_in_row, change_in_column in directions:
        new_row = row + change_in_row
        new_column = column + change_in_column

        while 0 <= new_row < BOARD_SIZE and 0 <= new_column < BOARD_SIZE:
            if board[new_row][new_column] == " ■ ":
                return False
            if board[new_row][new_column] == " ~ " or board[new_row][new_column] == " x ":
                break
            new_row += change_in_row
            new_column += change_in_column

    return True


def mark_destroyed(board, row, column):

    ship_cells = [(row, column)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for change_in_row, change_in_column in directions:
        new_row, new_column = row + change_in_row, column + change_in_column
        while 0 <= new_row < BOARD_SIZE and 0 <= new_column < BOARD_SIZE:
            if board[new_row][new_column] == " ■ ":
                ship_cells.append((new_row, new_column))
            else:
                break
            new_row += change_in_row
            new_column += change_in_column

    for new_row, new_column in ship_cells:
        for i in range(new_row - 1, new_row + 2):
            for j in range(new_column - 1, new_column + 2):
                if 0 <= i < BOARD_SIZE and 0 <= j < BOARD_SIZE:
                    if board[i][j] == " ~ ":
                        board[i][j] = " x "