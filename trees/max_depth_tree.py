'''
UMPIRE
U:
    given the root of a binary tree
    return its max depth
    max depth: the number of nodes along its path 
    [1,2,3] 
    output:
    2
M:
    in order traversal 
P:
    create a helper function
        if root is empty just return
        keep track of the maxium rescursed subtrees 
        of both left and right
        return the final number 
    call the helper funciton 
'''
def maxDepth(root):
    maxVal = 0
    def helper(root):
        if root is None:
            return
        maxVal = max(maxVal, max(helper(root.left) + 1, helper(root.right) + 1))
        return maxVal
    helper(root)
