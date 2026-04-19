# O(n) because each pointer moves once across the array
# Space is O(1) (you’re right there)

def twoSum(numbers, target):
   l,r = 0,len(numbers)-1
   while True:
      if numbers[l] + numbers[r] == target:
         return [l,r]
      if numbers[l] + numbers[r] > target:
         r -= 1 
      elif numbers[l] + numbers[r] < target:
         l += 1
      else:
         l += 1
         r -= 1
      
