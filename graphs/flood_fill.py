'''
UMPIRE
U:
    in a m x n grid called image
    starting at image sr,sc
    varaible color 
    change color if and only if 
        1. the starting pixel neighbors and itself are not already color
        2. do the same the thing horiontally and vertically to neighboring nodes
        3.  explore all paths stop when there are no more adjacnent pixels of the
            starting point
M: 
    dfs
P:
    run a dfs on the image grid
    stop if and only if we visited the node already 
    the color of the starting node doesn't match its neighbor or node we will explore
    look at up left down right paths 
    else keep exploring recursively 
'''
def floodFill(image, sr, sc, color):
    visit = set()
    origin = image[sr][sc]
    ROWS, COLS = len(grid), len(grid[0])

    dfs(sr,sc):
        if (sr,sc) in visit or image[sr][sc] != origin or sr < 0 or sr >= ROWS or sc < COLS or sc >= COLS:
            return 

        visit.add((sr,sc))
        image[sr][sc] = color
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr,dc in directions:
            nR, nC = dr + r, dc + c
            dfs(nR, nC)

    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) not in visit and iamge[sr][sc] == origin:
                dfs(r,c)

