'''
RAMPER
R - restate the problem
   given an integer array nums 
   return a new array 
   where each element is product of all lements in the orginal array except the current position were on when in the lists 
   algorithm must be written in O(n) time 
A - ask any questions 
   no questions right now 
M - make an example
   [1,2,3]
   [6,3,2]
P - pick a pattern
   prefix & postfix traverseals to get the correct output
E - explain the plan
   im going to take the product of everything but the current from left ro right will have it be the size of the original array in 1's
   and store it in a prefix sum array
   vice versa for postfix 
   then 
   multiply the arrays together to get the final output
   [1,2,3]
   prefix = [6,3,1]
   postfix = [1,1,2]
   final res = [6,3,2]
'''
def productExceptSelf(nums):
   ans = [1] * len(nums)
   total = 1

   postTotal = 1
   for idx in range(len(nums)-1,-1,-1):
      ans[idx] = postTotal
      postTotal *= nums[idx]


   for idx in range(len(nums)):
      ans[idx] = postTotal
      postTotal *= nums[idx]


   return ans 



