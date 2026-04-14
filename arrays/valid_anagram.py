
def validAnagram(s,t):
   if len(s) != len(t):
      return False

   freqMapS = {}
   for letter in s:
      if letter not in freqMapS:
         freqMapS[letter] = 1
         continue 
      freqMapS[letter] += 1

   for letter in t:
      if letter not in freqMapS:
         continue 

      freqMapS[letter] -= 1
      if freqMapS[letter] == 0:
         del freqMapS[letter]
         

   return len(freqMapS) == 0

'''
use alpha array to save on space since you can just alpha characeters 
and return False if any of them freqeuencies is not 0

 if len(s) != len(t):
        return False

    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    # instead of all()
    for num in count:
        if num != 0:
            return False

    return True
'''
