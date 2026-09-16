'''
RAMPER
R - restate the problem 
   given an array of heights
   return the the maxium area two endpoint can create
   height is length * width 
   width being the height 
   and the length is the range + 1 for the 0 based index 
A - ask any questions 
   will there always be a solution?
M - make an example
   [1,1,5,7,8,9,10]
   ans = []
   [1,2,2,310,500,2]
   ans = [310]
E - explain the plan
   find the max intial height 
   add up the length or range of numbers folowing the max heihg
   than multiple the length, range, with the min of the two endpoint heights 
   range would be a -1 i beleieve 
'''
def maxArea(height):
   maxArea = 0
   left,right = 0, len(height)-1
   while left < right:
      window = (right - left)
      maxArea = max(maxArea, (window * min(height[left],height[right])))

      if height[left] < height[right]:
         left += 1
      else:
         right -= 1
   return maxArea


         

