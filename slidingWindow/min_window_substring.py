'''
UMPIRE
U:
    given two strings s and t of diffent lengths
    return the minium window substring that every cahcaracyer in t 
    is included in that window 
    return an empty string if none of these requriements are met
M:  
    frequency hashmap
    sliding window

P:
    
    frequency hashmap
    for s and t
    utilize two pointers to build a sliding window
    we contiulsy move right
    we move left if and only if the frequenecy hashmaps of t are all in s 
        but before moving left track minium window seen so far
    return min window seen so far
'''
def minwindow(s,t):
    wantmap = {}
    for letter in t:
        wantmap[letter] = wantmap.get(letter,0) + 1
    left = 0
    havemap = {}
    have = 0
    need = len(wantMap)
    minwindowsubstring = float('inf')
    for right in range(len(s)):
        havemap[s[right]] = havemap.get(s[right],0) + 1

        if s[right] in wantMap and wantMap[s[right]] == haveMap[s[right]]:
            have += 1
        while have == need:
            minwindowsubstring = min(minwindowsubstring, ((right - left) + 1))
            havemap[s[left]] -= 1
            if s[left] in wantMap and wantMap[s[left]] < haveMap[s[left]]:
                have -= 1
            if havemap[s[left]] == 0:
                del havemap[s[left]]
            left += 1
    return minwindowsubstring

