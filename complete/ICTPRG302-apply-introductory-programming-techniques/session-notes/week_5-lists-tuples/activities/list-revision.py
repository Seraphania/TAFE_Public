# tic_tac_list
#            0     1    2
tic_tac = [['-',  'X', 'O'],  # 0
           ['X',  '-', 'X'],  # 1
           ['O',  '-', 'O']]  # 2

# given the list above, that represents
# a tic-tac-toe board's state
# do the following:
# (1) print the middle row
print(tic_tac[2])
# (2) print the dash on the middle row
print(tic_tac[1][1])
# (3) replace one dash such that X wins
tic_tac[1][1] = 'X'
print(tic_tac[1])
# (4) replace one dash such that O wins
tic_tac[2][1] = 'O'
print(tic_tac[2])
# (5) restore the board to its original state
tic_tac[1][1] = '-'
tic_tac[2][1] = '-'
print(tic_tac)

# # (6) create a function that accepts a board and a tuple (x, y)
# # and checks if a particular spot is unoccupied.
# # for example:
def is_space_free(board, coordinates):
      if (board[coordinates[0]][coordinates[1]]) == '-':
            return True # modify per spec
      else:
            return False
# such that:
print(is_space_free(tic_tac, (0, 0))) # True
print(is_space_free(tic_tac, (0, 1))) # False
print(is_space_free(tic_tac, (2, 1))) # True

# (7) create a function that checks if there are
# **any** unoccupied spaces on the board.
# Return True if there are empty spaces
#  Otherwise return false.
def has_free_spaces(board):
      for row in board:
            if '-' in row: # board[i][j]board[range(0, 3)][range(0, 3)]:
                  return True # modify as per rules above
                  break
            else:
                  return False

# for example:
print(has_free_spaces(tic_tac)) # returns True

# check that the function worked by modifying the board
# to a tied state (no winner)
# tic_tac_list
#            0     1    2
tic_tac = [['O',  'X', 'X'],  # 0
           ['X',  'O', 'O'],  # 1
           ['O',  'X', 'X']]  # 2
# now check that:
print(has_free_spaces(tic_tac)) # returns False

## Challenge!
# write code to convert this string
# into the list we started with:
tic_tac = ("- X O\n" +
           "X - X\n" +
           "O - O\n"   )

tic_tac_list = []
for line in tic_tac.splitlines():
      tic_tac_list.append(line.split())

print(tic_tac_list)



# scroll down for clues:



# you can split the string by each newline like so
#  tic_tac.splitlines()



# need more? keep scrolling!



# you can split each line into a list like so:
# tic_tac.split()



# need more? keep scrolling!



# create an empty list first:
# tic_tac_list = []



# now iterate over each line in the string



# for each line append the result of the split!