'''
RAMPER
R - restate the problem 
    return true or false depdnding on if one of the strings are 
    permuations of the other 
A - ask questions 
    don't have questions right now 
M - make an example 
    "em" "emi"
    true 
    "carbroken" "macbookbroken"
    false 
P - pick a pattern 
    hashmap / sliding window 
E - explain the plan 
    create a frequency hashmap of s1 
    for the length of s1 iterate s2 
    if any window the hashmap values turn to 0 
    return True 
    else return False 
'''
def checkInclusion(s1, s2):
    freqS1 = {}
    freqS2 = {}
    left = 0
    passed = False
    for letter in s1:
        freqS1[letter] = freqS1.get(letter,0) + 1
    for right in range(len(s2)):
        freqS2[s2[right]] = freqS2.get(s2[right], 0) + 1
        while right - left + 1 > len(s1):
            freqS2[s2[left]] -= 1
            if freqS2[s2[left]] == 0:
                del freqS2[s2[left]]
            left += 1
        if (right - left + 1) == len(s1):
            if freqS2 == freqS1:
                return True
    return False
