# O(n*k) instead of O(n * k log (k)) sorting algorithm

def groupAnagrams(strs):
   myMap = defaultdict(list)
   for s in strs:
      char = [0] * 26
      for letter in s:
         idx = ord(letter) - ord('a')
         char[idx] += 1
      myMap[tuple(char)].append(s)
   return list(myMap.values())
