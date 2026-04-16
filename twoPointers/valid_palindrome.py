# O(n) time no space is used

def isPalindrome(s):

   i,j = 0, len(s) - 1

   while i < j:

      if not s[i].isalphanum():
         i += 1
         continue 

      if not s[j].isalphanum():
         j -= 1
         continue 

      if s[i].lower() != s[j].lower():
         return False

      i += 1
      j -= 1

   return True

