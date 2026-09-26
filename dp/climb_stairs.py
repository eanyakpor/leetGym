'''
UMPIRE
U:
    there are n total stairs
    you can either take 1 or 2 steps
    track the amount of ways you can reach n stairs
    i.e.
        n = 2 
        ans = 2 
        1 step + 1 step
        or 
        2 step
    would the input ever be empty? no
M:
    recusion
P:
    recusivelyt decement n 1 or 2 times 
    until n becomes 0 
    keep track of the continuting sum of steps 
    
'''
