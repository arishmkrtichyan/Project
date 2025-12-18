from src.ship_input import coordinates
from src.game_logic import shot
from src.utils import print_board

def player_turn(board):
    while True:
        user_input = input("Ваш ход (например A1): ")
        result = coordinates(user_input)
        if result is None:
            continue
        row,col = result
        res = shot(board,row,col)
        return res