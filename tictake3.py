
# make a board that can accept placeholders
board_overlay = """
  {} | {} | {}
  ---+---+---
  {} | {} | {}
  ---+---+---
  {} | {} | {}
"""

# print(board_overlay)


def game_set_up():
    board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    game_play(board_spaces)

# beware the non reseting board


# print(board_spaces)
#
# print(board_overlay.format(*board_spaces))

# board_spaces[2] = "X"
# board_spaces[2] = "O"
# board_spaces[0] = "X"
# board_spaces[3] = "X"
# print(board_spaces)
#
# print(board_overlay.format(*board_spaces))


def board_update(board_overlay, board_spaces):
    print(board_overlay.format(*board_spaces))
    return board_overlay.format(*board_spaces)


# print(board_spaces)
#
# board_update(board_overlay)
# board_spaces[5] = "Hello"

#
# current_board = board_update(board_overlay)


def x_or_o(count):
    if count % 2 == 0:
        player = "O"
        return player
    else:
        player = "X"
        return player


# def move_select(player):


def turn(count, board_spaces):
    player = x_or_o(count)
    print("{} turn.".format(player))
    move = int(input("Pick a box: "))
    if move not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print("0-8")
        turn(count, board_spaces)
    elif board_spaces[move] == "X" or board_spaces[move] == "O":
        print("Already taken")
        turn(count, board_spaces)
    else:
        board_spaces[move] = "{}".format(player)


def end_game():
    print("Game over!")
    again = input("Do you want to play again? Y/n: ").lower()
    if again == "n":
        return False
    else:
        # game_play(board_spaces)
        game_set_up()


def win_check(board_spaces, winner):
    winner = True
    return winner
    if [board_spaces[space] for space in [0, 1, 2]] == ["X", "X", "X"]:
        print("X wins!")
        end_game()
    elif [board_spaces[space] for space in [0, 1, 2]] == ["O", "O", "O"]:
        print("O wins!")
        end_game()
    elif [board_spaces[space] for space in [3, 4, 5]] == ["X", "X", "X"]:
        print("X wins!")
        end_game()
    elif [board_spaces[space] for space in [3, 4, 5]] == ["O", "O", "O"]:
        print("O wins!")
        end_game()
    elif [board_spaces[space] for space in [6, 7, 8]] == ["X", "X", "X"]:
        print("X wins!")
        end_game()
    elif [board_spaces[space] for space in [6, 7, 8]] == ["O", "O", "O"]:
        print("O wins!")
        end_game()

    elif [board_spaces[space] for space in [0, 3, 6]] == ["X", "X", "X"]:
        print("X wins!")
        end_game()
    elif [board_spaces[space] for space in [0, 3, 6]] == ["O", "O", "O"]:
        print("O wins!")
        end_game()
    elif [board_spaces[space] for space in [1, 4, 7]] == ["X", "X", "X"]:
        print("X wins!")
        end_game()
    elif [board_spaces[space] for space in [1, 4, 7]] == ["O", "O", "O"]:
        print("O wins!")
        end_game()
    elif [board_spaces[space] for space in [2, 5, 8]] == ["X", "X", "X"]:
        print("X wins!")
        end_game()
    elif [board_spaces[space] for space in [2, 5, 8]] == ["O", "O", "O"]:
        print("O wins!")
        end_game()

    elif [board_spaces[space] for space in [0, 4, 8]] == ["X", "X", "X"]:
        print("X wins diagonally!")
    elif [board_spaces[space] for space in [0, 4, 8]] == ["O", "O", "O"]:
        print("O wins diagonally!")

    else:
        winner = False
        return winner
        return True


def game_play(board_spaces):
    playing = True
    xwins = False
    owins = False
    count = 0
    winner = False
    # board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board_update(board_overlay, board_spaces)
    while playing:
        count += 1
        turn(count, board_spaces)
        board_update(board_overlay, board_spaces)
        playing = win_check(board_spaces, winner)
        if count == 9 and not xwins and not owins:
            print("Draw")
            playing = False
    else:
        end_game()

# def check_wins():
#     if
#     if
#     if
#         return True
#
# game()
#     winning = False
#     while not winning:
#     while winning == False:
#         winning = check_wins()

game_set_up()
# game_play(board_spaces)
