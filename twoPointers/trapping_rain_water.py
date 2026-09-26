'''
UMPIRE
U:
   given a non negative integer array 
   where each bar is 1 
   compute the total amount of water that can be trapped
M: 
   two pointers 
P:
   utilize two pointers
   if left boundary is < right boundary
   move left and right up so we can find a spot where water doesn't overfill 
   once we see abigger point than right move left boundary there
   so we can keep progessing a potentaitl total of water trapped in the input 
   water trapped can be calcuated 
   when we have two valid points 
   min height + 

   don't readjust two pointers 
   until we reach a right boundary thats greater than left bounary
   keep an acumation all pockets that can have water
   the pockets that can have water are
   ends where the left bounday and the right boardry are the same    or 
   
'''
def trap(height):

