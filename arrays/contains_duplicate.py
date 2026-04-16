# time: O(n)
# space: O(n)
def containsDuplicate(nums):
   mySet = set()
   for n in nums:
      if n in mySet:
         return True
      mySet.add(n)
   return False
