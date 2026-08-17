'''
RAMPER
R - restate the problem 
    each row must contain digits 1 - 9 without repetition 
    column muist contains the same 
    each of the nine 3x3 must contains digits 1-9 without repetioin too 
    return true or false if it matches this case 
    only care about filled cells 
    cells not filled have a .
A - ask 
    any time / space constrinats board is 9 by 9 - not that great of a question tbh 
M - make example 
    [['5','.','5']]
    false 
P - pick a patter
    hashset for unqiue 
    quick lookup time and in its nature to be unique 
E - explain the plan 
    for each row build a hashset
    traverse by row if len of that rows doesn't match the hashset of that row 
    return False 
    do the same for columsn

    for the 3x3 
    traverse the 3 x 3 of each square create a hashaset 
    for the row and col if the len differes compared to the hashset reutrn False 
'''
def isValidSodoku(board):
    # check rows if their unique 
    for r in range(len(board)):
        seen = set()
        for c in range(len(board[0])):
            if board[r][c] == '.':
                continue
            if board[r][c] in seen:
                return False
            seen.add(board[r][c])
    
    for c in range(len(board[0])):
        seen = set()
        for r in range(len(board)):
            if board[r][c] ==  '.':
                continue
            if board[r][c] in seen:
                return False
            seen.add(board[r][c])
    
    setTwoDList = [[set() for _ in range(3)] for _ in range(3)]
    for r in range(len(board)):
        for c in range(len(board[0])):
            cell = board[r][c]
            if cell == '.':
                continue 
            box_row = (r//3)
            box_col = (c//3)
            if cell in setTwoDList[box_row][box_col]:
                return False
            setTwoDList[box_row][box_col].add(cell)
    return True


