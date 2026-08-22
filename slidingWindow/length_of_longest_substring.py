'''
RAMPER
R - restate the problem 
    given a string 
    return the longest substring without any dupoleicate fcharacters 
A - ask any question 
    no questions currentlyt 
M - make an example 
    "emilovescoding"
    ans = 15
    ""
    ans = 0
P - pick a pattern
    "abcabcbb"
       i 
     set = {a,b,c}
     "pwwkew"
          i
      set = {p,w,k,e}
      would be 4 
      but thtas not right awsner 
      as we've broken our window to add to our set 
      the correct awnser is 3 "wke"
E - explain the plan
    we will have two pointers 
    "pwwkew"
     l r
     if r is the same as r - 1 or better yet if r is in a set
     what if we had a set as our window any time we see ac hactere we've already added to our set clear the set then 
     slide l to r 
        add to longest length max tracker 
    return longest length substring 
pwwkew
     l
     r
w = {}
longest = 3 
'''
def lengthOfLongestSubstring(s):
    window = set()
    left = 0
    longest = 0
    for right in range(len(s)):
        # need to loop through window and remove all the characters and reset 
        if s[right] in window:
            window.clear()
            left = right 
            
        longest = max(longest, (right - left) + 1)
        window.add(s[right])
    return longest


        

    
