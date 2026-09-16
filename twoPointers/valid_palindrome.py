'''
UMPIRE
U:
   a string is a palindrome if and only if it reads the smae
   forwards and backwards
   convert all upper case letters to lower case letters too
   you can skip if the character is non alphanumreic
   
M - two pointers
P - 
   because the string can contain uppercase letters just make it into all lowercase letters 
   utilize two pointers each at one end 
   if we see a non alphanuremic character skip it
I - 
'''

def isPalindrome(s):
   left, right = 0, len(s)-1
   lowerS = s.lower()
   while left < right:
      if not lowerS[left].isalnum():
         left += 1
      if not lowerS[right].isalnum():
         right -= 1
      if lowerS[left] != lowerS[right]:
         return False
      left += 1
      right -= 1 
   return True 

