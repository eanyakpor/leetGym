'''
RAMPER

R - restate the problem 
   given an nums array. calculate the max amount of wat that can be stored in the list. 1 or > vlaue has width of 1 
A - ask any questions 
   don't have any questions right now
M - make an example 
   [1]
   0
   [1,3]
   2
P - pick a pattern
   two pointers / traversal
E - explain a plan 
   [4,2,0,3,2,5]
   i      j
   total = 2 


'''
def trap(height):
   total = 0
   i,j = 0, len(height)-1
   max_left = 0
   max_right = 0
   while i < j:
      max_left = max(max_left, height[i])
      max_right = max(max_right, height[j])
      if max_left <= max_right:
         total += (max_left - height[i])
         i += 1
      else:
         total += max_right - height[j]
         j -= 1

   return total
