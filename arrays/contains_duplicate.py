'''
time
O(N)
space
O(N)

for worst case
because at most we save all elements since there non unique 
and iterate though all elements since there non unique 
'''
def containsDuplicate(nums):
    mySet = set()
    for n in nums:
        if n in mySet:
            return True 
        mySet.add(n)
    return False

