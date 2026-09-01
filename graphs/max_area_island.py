'''
RAMPER
R - restate the problem 
    given a group of 1's 0's
    1's represent islands
    return the max number of islands 
    if there are no islands return 0
A - ask any questions 
    none at this momemnt 
M - make an example
    grids are to large to make just a test input tbh 
P - pick a pattern
    dfs
E - explain the plan
    traverse the grid
    if we see a 1 do dfs
    keep track of what has been visited in set
        in the dfs if we see a 1 return a 1 
    outside the dfs we will have a max tracker 
    to keep track fo the isalnd we visited with max 1s 

'''
def maxAreaOfIsland(grid):

    ROWS = len(grid)
    COLS = len(grid[0])
    visit = set()
    maxCount = 0 
    
    def dfs(r,c,visit):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visit or grid[r][c] == 0:
            return 0 
        visit.add((r,c))
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        area = 1 
        for dr,dc in directions:
            newR, newC = dr+r, dc+c
            area += dfs(newR, newC,visit)
        return area

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r,c) not in visit:
                maxCount = max(maxCount,dfs(r,c,visit))
    return maxCount
