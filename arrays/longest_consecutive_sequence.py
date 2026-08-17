
'''
RAMPER

R - restate the problem 
   given an array of nums 
   return the length of longest consecutive sequence 
   algorithm must be in O(n) time 
A - ask questions 
   can't think of a unique case to be honest where i don't understand 
   duplicates wouldn't matter for this problem were keeping of the longsst conseutive sequence and if the numbers are the same there considers the same number and should be repsresnted as that 
   i have a question now will there always be an awsner 
   seems not 

M - make example
   [1,2,3,4]
   ans = 4 
   [4,3,1020,20,1,2]
   ans = 4
P - hashing for quick lookup time 
    set 
E - explain the plan 
   im going to the input into a set 
   and check for element - 1 of it 
   set = [4,3,1020,20,1,2]
   if - 1 for that is present add to a maxium length tracker
   return the maxium length tracker at the end 
   set = [100,4,200,1,3,2]
                  i
   set = {100,4,200,1}
   mLen = 3

   i think a better approach would be find the start so minium value in the list than start adding 1 to see how many times we see it in our input 
   keep track of that increment in our maxium length currently variable 


   set = [100,4,200,1,3,2]
                    i
   is 100 -1 present in the array ?
   its not min move i
   keep adding + 1 to min until that number is not present
   keep track of the max of it as we want the longest possible 
   just any consecutive sequence but the longest vesion of that
   [100,4,200,1,3,2]
   [0,3,7,2,5,8,4,6,0,1]
'''
def longestConsecutive(nums):
   num = set(nums)
   maxLen = 0
   for n in num:
      if (n - 1) not in num:
         min = 1
         while min + n in num:
            min += 1

         maxLen = max(maxLen,min)
   return maxLen

