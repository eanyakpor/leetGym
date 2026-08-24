'''
RAMPER
R - restate the problem 
    given an interger array nums 
    and an integer k 
    for each window lenth k return that in a new array in its ith position
A - ask questoin 
    does order matter?
M - make an example 
    [1,1,1,1,1,1,1]    K =4
    [1]
P - pick a pattern 
    sliding window 
E - explain the plan
    traverse k lengths w/ right pointer 
    have left iterate to find cuyrring windows max pointer
        append that max we foundin the k length window into res array
    adjust left to point to right 
'''
def maxSlidingWindow(nums,k):
left = 0
    res = []
    for right in range(len(nums)):

        # once our window reaches size k
        if (right - left) + 1 == k:
            maxVal = float('-inf')

            # scan every element inside the current window
            for i in range(left, right + 1):
                maxVal = max(maxVal, nums[i])

            # save this window's maximum
            res.append(maxVal)

            # slide the window forward by one
            left += 1

    return res


