# O(n) solution
# we want product of everything LEFT × product of everything RIGHT
def productExceptSelf(nums):
   front = [1] * len(nums)
   back = [1] * len(nums)
   ans = [0] * len(nums)
   prod = 1

   for idx in range(len(nums)):
      front[idx] = prod
      prod *= nums[idx]
   print('front',front)
   prod = 1

   for idx in range(len(nums)-1,-1,-1):
      back[idx] = prod
      prod *= nums[idx]
   print('back',back)

   for i in range(len(front)):
      ans[i] = (front[i] * back[i])

   print('a',ans)
   return ans 

'''
O(1) solution
def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n

    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans
'''
      
      


