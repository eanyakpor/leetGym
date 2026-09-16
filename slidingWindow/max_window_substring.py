'''
UMPIRE
U:
    you are given an array of integrs
    there is a sliding window of size k
    in each window of size k save the max element 
    and return that in an array
M:
    sliding window
P:
    utilzie two pointers
    keep track of max number visited
    if and only if the size of the window is > k 
        append max number visited in res array 
        move left 
        reset max Number
'''
def maxSlidingWindow(nums,k):
    left = 0
    maxValue = float('-inf')
    res = []
    if len(nums) == 1:
        return [nums[0]]
    for right in range(len(nums)):
        if ((right - left) + 1) > k:
            res.appnd(maxValue)
            left += 1
            maxValue = float('-inf')
        maxValue = max(maxValue, nums[right]
    return res

