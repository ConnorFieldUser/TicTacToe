
# make a board that can accept placeholders
board_overlay = """
  {} | {} | {}
  ---+---+---
  {} | {} | {}
  ---+---+---
  {} | {} | {}
"""

# print(board_overlay)


# beware the non reseting board

board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]

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


def board_update(board_overlay):
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


def turn(count):
    player = x_or_o(count)
    print("{} turn.".format(player))
    move = int(input("Pick a box: "))
    if board_spaces[move] == "X" or board_spaces[move] == "O":
        print("Already taken")
        turn(count)
    else:
        board_spaces[move] = "{}".format(player)


def end_game():
    print("Game over!")
    again = input("Do you want to play again? Y/n: ").lower()
    if again == "n":
        print("Goodbye")
        playing = False
    else:
        game_play()


def win_check(board_spaces):
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


def game_play():
    playing = True
    count = 0
    board_update(board_overlay)
    board_spaces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while playing:
        count += 1
        turn(count)
        board_update(board_overlay)
        win_check(board_spaces)

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

game_play()
