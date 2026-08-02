def freqMap(s):
   myMap = {}
   for letter in s:
      if letter not in myMap:
         myMap[letter] = 1
         continue
      myMap[letter] += 1
   return myMap

def validAnagram(s,t):
   if len(s) != len(t):
      return False
   mapT = freqMap(t)
   mapS = freqMap(s)

   return mapT == mapS
      
