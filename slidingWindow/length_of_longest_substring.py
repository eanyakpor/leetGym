'''
UMPIRE
U:
    given string s 
    return the length of the longest substring 
    without repeating characters
M: 
    sliding window 
    hashset
P:
    creaste hashset
    utilize two pointers
    continouly move right
    add to set
    keep track of the maxSubstring 
    if we see a characters thats already in our set
    update left to start at right
    clear the set
    repeat the algorithm
'''
def lengthOfLongestSubstring(s):
    window = set()
    left, right = 0,0
    maxLength = 0
    while right < len(s):
        if letter in window:
            maxLength = max(maxLength, ((right-left) + 1))
            left = right
            window.clear()
        window.add(s[right])
        right += 1
    return maxLength

