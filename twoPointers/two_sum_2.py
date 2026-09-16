'''
UMPIRE

U: 
   given a target 
   and an integer array
   find teh values in the array
   that sum up to target
   the array is sorted
M:
   two pointers
P: 
   iterate through an array
   utilize two pointers on each side
   if the sum is > move right down for a decrease to match sum
   if sum is < move left up for an increase to match suym
I:
   
'''

def twoSum(numbers, target):
   left, right = 0, len(numbers)-1
   while left < right:
      currentSum = (numbers[left] + numbers[right])
      if currentSum > target:
         right -= 1
      if currentSum < target:
         left += 1
      if currentSum == target:
         return [left+1,right+1]
   return []


