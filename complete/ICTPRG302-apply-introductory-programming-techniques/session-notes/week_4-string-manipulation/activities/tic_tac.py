tic_tac = (    "- X O\n" +
               "X - X\n" +
               "O - O\n"  )

# what is the length of the string?
print(len(tic_tac))

# make the following print True by substituting
# each `?` with a **different** value
# NOTE: **all** you need to do is substitute the `?` with integers!
print(tic_tac[0] ==
      tic_tac[8] ==
      tic_tac[14]) # True

print(tic_tac[2] ==
      tic_tac[6] ==
      tic_tac[10]) # True

print(tic_tac[5] ==
      tic_tac[11] ==
      tic_tac[17]) # True

# combine two slices of the original string
# for X to win the game:
print(tic_tac[6:8] + 'X' + tic_tac[9:11])

# combine two slices of the original string
# for O to win the game:
print(tic_tac[12:14] + 'O' + tic_tac[15:17])

# Bonus: Complete the following to print "XXX":
print(tic_tac[2:11:4])