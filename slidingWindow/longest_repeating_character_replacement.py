'''
RAMPER 
R - restate the problem
    return the longest subtstring 
    that contians the same letter 
    your a given a k that allows you to skip a character that doens't match the current subtring inwdow 
A - ask any qiestions 
    none right now 
M - make an example 
    "EMII" k = 1 
    ans = 3 
    "CHARLENE" k = 3
    4 
P - pick a pattern
    build frequency hashmnap for a window 
    keep increasing window to the right if k > 0 k times
    keep track of longest window thats in the window and doesn't over k times 
    ABAB
       r
       l
    count = k = 0
    AABABBA
    l
       r
    
    count = k = 0
    mL = 3 
'''
def characterReplacement(s,k):
    window = {}
    maxFreq = 0
    maxLongest = 0
    left = 0
    for right in range(len(s)):
        window[s[right]] = window.get(s[right],0) + 1
        maxFreq = max(maxFreq, window[s[right]])
        while ((right - left) + 1) - maxFreq > k:
            window[s[left]] -= 1 
            left += 1
        maxLongest = max(maxLongest, ((right - left) + 1))
    return maxLongest

