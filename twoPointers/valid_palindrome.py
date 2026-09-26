'''
RAMPER
R - restate 
   going forward backaward doesn't matter with palindromes! 
   since they'd be the same
   remove alphanumerica characters convert upper case to lower case to potetnially achiee a plaindrome 
   returns a true if palindrome or false if not
A - ask a question 
   can't think of critical thinking question constraints awsnered most of it on leetcode 
M - make an example
   emi. can. run
   emicanrun
   False
   baaabbb....babbbb
   False
   baab
   True
P = pick a pattern 
   going to strip the string to non alphanumic characters
   or just skip over them 
   remove spacing and punciton or just skip over them
   going to use two pointers 
   from both ends if at any point s[i] != s[j] return False
E - explain the plan 
   going to strip the string to non alphanumic characters
   or just skip over them 
   remove spacing and punciton or just skip over them
   going to use two pointers 
   from both ends if at any point s[i] != s[j] return False
R - review
A man, a plan, a canal: Panama
a man, a plan, a canal: panama
  i                          j

'''

def isPalindrome(s):
   newS = s.lower()
   i,j = 0, len(newS)-1
   while i <= j:
      if not newS[i].isalnum():
         i += 1
         continue
      if not newS[j].isalnum():
         j -= 1
         continue
      #print('s[i]',newS[i])
      #print('s[j]',newS[j])
      if newS[i] != newS[j]:
         return False
      i += 1
      j -= 1
   return True
