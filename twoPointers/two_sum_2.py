'''
RAMPER

R - restate the problem 
   given a sorted list in ascending order 
   find twoi numbers that sum up to target 
   result must be indicies 
   the nums array starts at 1 instead of 0 
   ensure indicies are respetinve their position in the array 
   wehre the output reflects indeix i is < index j alwayus 
A - ask question 
   nothing right now 
   can there be duplicates in this input ?
M - make an example
   [1,3,4,5]
   target = 5
   [1,3]
E - explain a plan 
   create two pointers 
   [1,3,4,5]
    i j
    since its sorted adjust j to be move right if the total is < target else move j to the left 
    theres always a unique solution for this problem 
    to enswure we don't use the exact indcie twice 
    check if the prev if i > 0 for i and j next thats not  the same element 
R - review
target = 5
[1,3,4,5]
 i     j
 total = 6

[1,3,4,5]
 i   j

'''

def twoSum(numbers, target):
   idx,j = 0,len(numbers)
   while idx < j:
      total = (numbers[idx] + numbers[j])
      if total > target:
         j -= 1
      elif total < target:
         idx += 1
      else:
         while idx > 0 and numbers[idx] == numbers[idx-1]:
            idx += 1
         while idx < j and numbers[j] == numbers[j+1]:
            j -= 1
         return [(idx+1),(j+1)]
