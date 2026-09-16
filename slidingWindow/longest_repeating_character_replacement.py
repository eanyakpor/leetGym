'''
UMPIRE
U:
    given a strings s and integer k that allows skips basically 
    return the lenth of the longest substring that 
    that contain the same letter
M:
    hashmap for frequenct character 
    sliding window
P:
    keep track of max frequenct chcarcater in string

    utilize two pointers
    while we find that the most frequenct chacter - size of window is greater than k 
    remove left chacacter from the hashmp 
    if left chacracter == 0 del
    move left 1 
'''
def characterReplacement(s,k):
    left = 0
    myMap = {}
    maxLength = 0

    for right in range(len(s)):
        myMap[s[right]] = myMap.get(s[right],0) + 1
        maxFreq = max(maxFreq, myMap[s[right]])
        while ((right - left) + 1) - maxFreq  > k:
            myMap[s[left]] -= 1
            if myMap[s[left]] == 0:
                del myMap[s[left]]
            left += 1
        maxLength = max(maxLength, ((right - left) + 1))


