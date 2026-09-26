'''
RAMPER
R - restate the problem 
    given an array of integers 
    return a new array where each ith position is the distance the original ith elment is from a higher temperate value 
A - ask any questions 
    don't have any questions right now
M - make an example 
    [75,73]
    [0,0]
P - pick a pattern 
    stack / sliding window or at least two pointers
E - explain the plan
    create res array filled with zeroes
    create stack 
    go through array with two pointers
    if we encounter an element > top of stack
    set res ith to the indicies of the stack 
    return res 
'''
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures) 
    stack = []
    for right in range(len(temperatures)):
        while stack and temperatures[right] > temperatures[stack[-1]]:
            prevIdx = stack.pop()
            res[prevIdx] = right - prevIdx
        stack.append(right)
    return res 

