# -*- coding: UTF-8 -*-

#task: From the following program, move functions move_player, move, move_ai a get_result to its own module
# then new module import and use function from it

import random

def move_player(game_board):
    while True:
        cell_number = input("Give number between 0-19: ")
        cell_number = int(cell_number)
        if cell_number < 0 or cell_number > 19:
            print("number must be between 0-19.")
        elif game_board[cell_number] != "-":
            print("cell  {} is full, please add different one.".format(cell_number))
        else:
            return move(game_board, cell_number, "x")

def move(game_board, cell_number, symbol):
    return game_board[:cell_number] + symbol + game_board[cell_number + 1:]

def move_ai(game_board):
    while True:
        cell_number = random.randrange(len(game_board))
        if game_board[cell_number] == "-":
            return move(game_board, cell_number, "o")

def get_result(game_board):
    if "xxx" in game_board:
        return "x"
    elif "ooo" in game_board:
        return "o"
    elif "-" not in game_board:
        return "!"
    else:
        return "-"

# 1-D TicTok is played on row between 0 - 19.
# Players adding  (o) and (x) one by one, for example:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Winner is player with 3 same symbols!

# Make a board plan

game_board = "-" * 20
on_move = "x"

while True:
    if on_move == "x":
        game_board = move_player(game_board)
        on_move = "o"
    elif on_move == "o":
        game_board = move_ai(game_board)
        on_move = "x"

    result = get_result(game_board)
    print(game_board)

    if result != "-":
        if result == "!":
            print("Draw! {}".format(game_board))
        elif result == "x":
            print("Winner is Man {}".format(game_board))
        elif result == "o":
            print("Winner is AI {}".format(game_board))
        else:
            raise ValueError("non-excepted game result '{}'".format(result))
        break