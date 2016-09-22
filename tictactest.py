brains = "BRAINS?"

stringy = "Hello. This is a testing file for testing {}."


print(stringy.format(brains))

# tic-tac-toe

test = "TESTING"
# print the board matrix
board = """
   0   1   2
A  {} | {} | {}
  ---+---+---
B  {} | {} | {}
  ---+---+---
C  {} | {} | {}
"""
# What moves are on the board?
# Who's turn is it?
# Is that a legal move?
# ask for input


# board_spaces = [test, a1=" ", a2=" ", b0=" ", b1=" ", b2=" ", c0=" ", c1=" ", c2=" "]
board_spaces = [" "] * 9
newboard = board.format(*board_spaces)
print(newboard)
# input("make your move. Pick a row: ")
# input("now pick a collumn: ")
x = "X"
o = "O"

board_spaces.insert(0, x)
board_spaces.insert(2, test)
board_spaces.insert(8, o)
# battleship coordinates
print(board.format(*board_spaces))
# add X,O to space
#
# check for turns
# listy = [a0=" ", a1=" ", a2=" ", b0=" ", b1=" ", b2=" ", c0=" ", c1=" ", c2=" "]

# check for wins between turns


# composability

# break apart the loop

# while:
# else:

# not top down; iterative
# inside out; now top down

# mutating player dicionary by side effect:
# changing dictionsary from insinde function
