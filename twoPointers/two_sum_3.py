'''
UMPIRE
U:
    given an intergar aray nums 
    return all triplets that sum to 0 
    ensure all indiices of the triplets are unique 
M: 
    sort then follow up with class two sum 2 algorithm 
    where you you change hi lo dpeneding how far the target is compared to the sum 
P - 
    sort the array 
    loop through the array
    ensure we are starting at a non duplication
    to avoid potential dupicates
    utilzie two pointers to traverse a window that is after position i
    now we are determing for each index what the two values sum up to target are and can append that to a set lists 
I - 
'''
def threeSum(nums):
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        left = i + 1
        right = len(nums) - 1
        while left < right:
            tripleSum = (nums[i] + nums[left] + nums[right])
            while left < right and nums[left] == nums[left+1] and tripleSum < 0: 
                left += 1 
            while left < right and and nums[right] == nums[right-1] and tripletSum > 0:
                right -= 1
            if tripleSum == 0:
                ans.append([nums[i],nums[left],nums[right]])
        return ans
                

