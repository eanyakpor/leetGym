'''
RAMPER
R - restate the problem
    each row must contain unique numbers 1 - 9
    each col must contain unique numbers 1 - 9
    in a 3x3 box there must bu unqie numbers 1-9
A - ask a question
    does each row have to contain 1 - 9 numbers
    or just be unique? - just be unique weak question 
M - make an example 
    follow input cause its large skipping
P - pick a pattern
    hashset 
    3 x 3 traversal pattern that flag non unqiue numbers 
E - explain the plan
    definetly create a set for the 9 rows and 9 cols 
    than just insert row wise and if we see any duplicates any
    numbers already in the set just flag it return False
    for the 3  x 3 
    we can do a 3 x 3 traversal 
'''
def isValidSodoku(board):
    rowSets = [set() for _ in range(9)]
    rowCols = [set() for _ in range(9)]
    boxSets = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue 
            if board[r][c] in rowSets[r]:
                return False

            rowSets[r].add(board[r][c])

    for c in range(9):
        for r in range(9):

            if board[r][c] == '.':
                continue 
            if board[r][c] in rowSets[c]:
                return False

            rowSets[c].add(board[r][c])

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue 
            if board[r][c] in boxSets[r // 3][c // 3]:
                return False

            boxSets[r // 3][c // 3].add(board[r][c])
    return True 
