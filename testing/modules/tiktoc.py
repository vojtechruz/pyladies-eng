# -*- coding: UTF-8 -*-
import random

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