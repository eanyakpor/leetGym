
'''
RAMPER
R - restate the problem 
   given an array nums return a new array thats content is the product of all nums[i] constraint i the ith postioin doesn't include nums[i]
   so 
   [1,2,3,4]
   ans = [24,12,8,6]
A - ask questions 
   don't have any questions at the top of my head for this one not going to lie 
   leetcode platforms awsnered all my questions with its description tbh 
   idk if i should just not read leetcdeo descript constraints and just my ask question but thene again reading the problem finding your question isn't good by reading is a good skill to have 
M - make example 
   [2,3,3] 
   a = [9,6,6]
   pretty straight forward tbh
P - pseudocdoe
   [2,3,3]
   forward skip the ith current 
   [9,3,1]
   backward skip the ith current
   [6,2,1]
   a = [9,6,6]

   [1,2,3,4]
   a = [24,12,8,6]
   [24,12,4,1]
   [6,2,1,1]
   a = [24,12,8,6]
   created a forward product array that skips the current ith
   do the same for backward

   append the resultant awnsers as for forward array should multiple forward to the backward arrays reverse 
   so forwardly go through forward array times it by backward array in reverse
   return each element in new array for the awnser 
E - is the baove explain the plan for P pick a pattern im just dfoing traverslals of arrays 
[2,3,3]

'''
def productExceptSelf(nums):
   prefix = [1] * len(nums)
   suffix = [1] * len(nums)
   prodPrefix = 1
   for n in range(len(nums)):
      prefix[n] = prodPrefix
      prodPrefix *= nums[n]
   prodSuffix = 1
   for n in range(len(nums)-1,-1,-1):
      suffix[n] = prodSuffix
      prodSuffix *= nums[n]

   res = []
   for p,s in zip(prefix,suffix):
      res.append(p*s)
   return res 

      



