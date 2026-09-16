'''
RAMPER
R - restate the problem
   given an unsortd array
   return the length of the longest consecruvie sequence 
   algorithm must be written in O(N) time 
A - ask any question 
   are there any duplicates in input it wouldnt matter 
   actually since 2 2's are still 1 since theyd just be a represenation of a single 2 
M - make an example 
   [4,3,2,1]
   4
E - explain the plan
   turn the input into a set for quick lookup time
   check if -1 is not in the input if True thats our starting point
      once we have reachd a valid start
      while + 1 is in the input
         increment
         keep track of max length
      add to set always 
   [100,4,200,1,3,2]

'''
def longestConsecutive(nums):
   numSet = set(nums)
   maxLength = 0

   for n in numSet:
      if n - 1 not in numSet:
         currentNum = n
         count = 0
         while currentNum in numSet:
            count += 1
            maxLength = max(maxLength, count)
            currentNum += 1 
   return maxLength



