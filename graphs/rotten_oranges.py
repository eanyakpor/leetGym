'''
RAMPER
R - restate the problem
    every minute 
    a new orange turns rotten 
    return the minium number of elpased time 
    it takes for all ornages to be rotten
    0: an empty cell
    1: fresh orange
    2: rotten orange
A - ask any question 
    none at the moment
M - make an exmaple
    followed lc exmaple instead
P - pick a pattern
    bfs
E - explain the pattern
    traverse the grid starting at a fresh orange, 1 
    while q isn't empty
    pop that cell than change 1's to 2's to spread the disease 
    check in four directions to spread disease 
        add back onto the queue fresh orange if its is 
        ensure were at a valid cell before we convert fresh to orange
    count += 1
    return global count after checking all four directions in bfs 
'''
def orangeRotting(grid):
    queue = deque()
    ROWS = len(grid)
    COLS = len(grid[0])
    visit = set()
    minutes = 0
    fresh = 0

    # put rotten oranges in q 
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 2:
                queue.append((row,col))
                visit.add((row,col))
            elif grid[row][col] == 1:
                fresh += 1
    # traverse q 
    while queue fresh > 0:

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # traversing rotten oranges in q
        for _ in range(len(queue)):
            r,c = queue.popleft()
            for dr,dc in directions:
                nR, nC = dr + r, dc + c
                if nR < 0 or nR >= ROWS or nC < 0 or nC >= COLS  or grid[nR][nC] == 0 or grid[nR][nC] == 2:
                    continue 
                grid[nR][nC] = 2
                fresh -= 1
                queue.append((nR,nC))
                visit.add((nR,nC))
            minutes += 1
    if fresh > 0:
        return -1
    return minutes
                





