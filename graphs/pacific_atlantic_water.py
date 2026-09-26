'''
UMPIRE 
U:
    given a m x n grid
    and a pacific and atlics ocean
    find the cells that can go from pacific to antlics or vice versa 
M: 
    dfs
P:
    starting from pacific ocean and antlatic ocean
    save cells that are >= neighboring counterpearts
    putting those coordinates in a set
    do the same for antlics 

    compare both sets 
    and return the result at the end
'''
def pacificAtlantic(heights):
    pacific, antlantic = set(), set()
    result = []
    visit = set()
    ROWS, COLS = len(heights), len(heights[0])
    def dfsPacific(r,c, previousHeight):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit heights[r][c] < previousHeight:
            return
        visit.add((r,c))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr,dc in directions:
            newR, newC = dr + r, dc + c


            dfsPacific(newR, newC, previousHeight)


            pacific.add((newR, newC))


    def dfsAntlantic(r,c, previousHeight):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or height[r][c] < previousHeight:
            return

        visit.add((r,c))
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr,dc in directions:
            newR, newC = dr + r, dc + c


            dfsAntlantic(newR, newC,previousHeight)


            antlantic.add((newR, newC))
    # pacific ocean

    # top edge
    for col in range(COLS):
        dfsPacific(0,col,heights[0][col])

    # left most edge
    for row in range(ROWS):
        dfsPacific(row, 0, heights[row][0])

    # antlantic ocean

    # right most edge 
    for row in range(ROWS):
        dfsAntlantic(row, COLS - 1, heights[row][COL-1])

    # bottom row
    for col in range(COLS):
        dfsAntlantic(ROWS - 1, col, heights[ROWS-1][col])

    result = []

    for p,a in zip(pacific, antlantic):
        if p and a in pacific and p and a in antlantic:
            result.add((p,a))
    return result


