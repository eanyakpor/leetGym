
def lengthOfLongestSubstring(s):
   myMap = {}
       l = 0
       mx = 0

       for r in range(len(s)):
           letter = s[r]
           myMap[letter] = myMap.get(letter, 0) + 1

           while myMap[letter] > 1:
               left_char = s[l]
               myMap[left_char] -= 1
               l += 1

           mx = max(mx, r - l + 1)

       return mx
