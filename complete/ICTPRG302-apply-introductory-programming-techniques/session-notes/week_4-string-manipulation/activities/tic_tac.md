```python
tic_tac = (    "- X O\n" +
               "X - X\n" +
               "O - O\n"  )
```

1. What is the length of the string?  
   * insert code here

2. Make the following print True by substituting # each `?` with a **different** value  
   * *NOTE: **all** you need to do is substitute the `?` with integers!*
```python
print(tic_tac[0] ==
      tic_tac[?] ==
      tic_tac[?]) # True

print(tic_tac[2] ==
      tic_tac[?] ==
      tic_tac[?]) # True

print(tic_tac[5] ==
      tic_tac[?] ==
      tic_tac[?]) # True
```

3. combine two slices of the original string
   * for X to win the game:
```python
print(tic_tac[?:?] + 'X' + tic_tac[?:?])
```

4. combine two slices of the original string
   * for O to win the game:
```python
print(tic_tac[?:?] + 'O' + tic_tac[?:?])
```