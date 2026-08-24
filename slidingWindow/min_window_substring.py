'''
RAMPER
R -  restate the problem 
    given two strings s and t 
    of different sizes m and n 
    find and return the minium window substring of s that contains all of t include duplicates 
    if there is no substring return an empty string 
A - ask questions 
    don't have any questions right now 
M - make an example 
    t = 'emi' s = 'emiloves'
    ans = 'emi'
    t = 'looney' s = 'tunesofdoom'
    ans = ''
P - pick a pattern 
    sliding window hashmap 
E - explain the plan 
    create a hashmap of t 
    utilize two poiunters to slide window 
    adjust left if and only if the window has every character in our hashmap 
        keep track of the minium substring - if and only if all characters present in our window is in the hashmap 



'''
def minWindow(s,t):
    needMap = {}
    windowMap = {}
    for letter in t: 
        needMap[letter] = needMap.get(letter,0) + 1
    need = len(needMap)
    have = 0

    left = 0
    bestLen = float('inf')
    bestStart = 0

    for right in range(len(s)):
        windowMap[s[right]] = windowMap.get(s[right],0) + 1
        if s[right] in needMap:
            if windowMap[s[right]] == needMap[s[right]]:
                have += 1 
        while have == need: 
            if ((right - left) + 1) < bestLen:
                bestLen = ((right-left)+1)
                bestStart = left
            windowMap[s[left]] -= 1 

            if s[left] in needMap:
                if windowMap[s[left]] < needMap[s[left]]:
                    have -= 1 
            left += 1 
    if bestLen == float('inf'):
        return ''
    return s[bestStart:bestStart + bestLen] 




