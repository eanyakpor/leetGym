'''
UMPIRE
U:
    given a m x n grid 
    contains strings of only 0's and 1's
    1: land
    0: water

    return number of islands that are in the grid
M:
    count the number of connected components 1's in the grids
    dfs
P:
    traverse the array
        if we catch a 1 thats unvisited
            result = run a dfs - it will return 1 each time it explores a connected componit
    return result
'''

def numIslands(grid):

    result = 0
    ROWS,COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r,c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == "0":
            return 0
        
        visit.add((r,c))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr,dc in directions:
            nR, nC = dr + r, dc + c
            dfs(nR, nC) + 1


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visit:
                result += dfs(r,c)

