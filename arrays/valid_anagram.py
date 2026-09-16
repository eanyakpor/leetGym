
def validAnagram(s,t):
   if len(s) != len(t):
      return False
   
   myMap = {}
   for letter in s:
      if letter not in myMap:
         myMap[letter] = 1
      myMap[letter] += 1

   for letterTwo in t:
      if letterTwo in myMap:
         myMap[letterTwo] -= 1
         if myMap[letterTwo] == 0:
            del myMap[letterTwo]

   return True if len(myMap) == 0 else False
      
