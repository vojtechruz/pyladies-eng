# -*- coding: UTF-8 -*-

from tiktoc import move, move_player, move_ai, get_result

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