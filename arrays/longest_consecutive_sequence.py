# time O(n)
# space O(n)
def longestConsecutive(nums):
   newNums = set(nums)
   count = 0
   mx = float('-inf')
   for n in newNums:
      if (n-1) not in newNums:
         start = n
         # resets so everything starts from scratch no depenedy across solutions on eachoterh
         count = 0

         while start in newNums:
            start += 1
            count += 1

         # keeps track of best compelte length
         mx = max(mx,count)


   return mx
