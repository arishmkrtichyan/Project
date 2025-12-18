from src.ship_input import coordinates
from src.utils import empty_board, print_final_empty_board
from src.bot_generation import SeaBattleBot
from src.gameplay import player_turn
from src.game_logic import shot

def mark_surrounding(board, cells):
    """Помечаем 'x' вокруг всех клеток корабля"""
    for row_index, col_index in cells:
        for i in range(row_index - 1, row_index + 2):
            for j in range(col_index - 1, col_index + 2):
                if 0 <= i < 10 and 0 <= j < 10:
                    if board[i][j] == "~":
                        board[i][j] = "x"

def can_place_ship(board, start_row, start_col, length, direction):
    """Проверка, можно ли поставить корабль в заданной позиции"""
    ship_cells = []

    for k in range(length):
        if direction == "right":
            r, c = start_row, start_col + k
        elif direction == "left":
            r, c = start_row, start_col - k
        elif direction == "down":
            r, c = start_row + k, start_col
        elif direction == "up":
            r, c = start_row - k, start_col
        else:
            return None  # неверное направление

        if not (0 <= r < 10 and 0 <= c < 10):
            return None  # выходит за границы
        if board[r][c] == "■":  # нельзя ставить на чужой корабль
            return None
        ship_cells.append((r, c))

    # Проверяем соседние клетки каждой части корабля только на наличие других "■"
    for r, c in ship_cells:
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i < 10 and 0 <= j < 10:
                    if board[i][j] == "■" and (i, j) not in ship_cells:
                        return None  # соседний корабль мешает

    return ship_cells

def place_multicell_ship(board, length):
    while True:
        print_final_empty_board(board)
        start_input = input(f"Enter start coordinate for {length}-cell ship: ")
        start_coord = coordinates(start_input)
        if start_coord is None:
            continue

        start_row, start_col = start_coord
        direction = input("Enter direction (up, down, left, right): ").lower()

        ship_cells = can_place_ship(board, start_row, start_col, length, direction)
        if ship_cells is None:
            print("Cannot place ship here. Try another position or direction.")
            continue

        # Ставим корабль
        for r, c in ship_cells:
            board[r][c] = "■"

        mark_surrounding(board, ship_cells)  # помечаем окружающие клетки "x"
        break

def place_single_ships(board, count):
    placed = 0
    while placed < count:
        print_final_empty_board(board)
        user_input = input(f"Place single-cell ship ({placed+1}/{count}): ")
        result = coordinates(user_input)
        if result is None:
            continue

        r, c = result
        if board[r][c] != "~":
            print("Cannot place ship here!")
            continue

        board[r][c] = "■"
        mark_surrounding(board, [(r, c)])
        placed += 1

def main():
    battleship_board = empty_board()

    # 1-ячейковые
    place_single_ships(battleship_board, 4)

    # 2-ячейковые
    for _ in range(3):
        place_multicell_ship(battleship_board, 2)

    # 3-ячейковые
    for _ in range(2):
        place_multicell_ship(battleship_board, 3)

    # 4-ячейковый
    place_multicell_ship(battleship_board, 4)

    print("All ships placed!")
    print_final_empty_board(battleship_board)

if __name__ == "__main__":
    main()


             


