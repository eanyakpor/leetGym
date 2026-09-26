'''
R - read the 'problem' aloud content is usually generated to be large just need to repeat the problem identifying the only blocker for understading to finding the solution 
P - find problem 
Q - active questions - come with a question with a potenital prepared example or indept thought process 
match - W/ Potnetial data structure or coding algorthim 
pseudocode - english lettering for potetnial solution ensure alignment with interviewer before the start t ocoding 
review - time/space complexity, how to optizme what are better solutions 

Problem: need to return an 2d array that groups anagrams of the the given list strs

[""] -> [[""]]
is it only english letters? - yes lowercase lettering
any time constraints? - yes solution must be < 10^4 so a O(N) solution will be able to work here 

brute force 
have the default value of the hashmap list be a list
I would just iterate 
    sort each work and represent that as the key,tuple, in hashmap
    save the value of the hashmap to be a list of elements that match the sorted element to key 
return hashmap values that should be a list of nested elements per sorted key and tuple 

optimal 
because the brute force sorts every element in the list 
sorting takes O(log(n)) so on eachn element is O((log(n^2)))
we can remove the sorting 
by matching to see if the keys ascii values in our list of ascii values are repsrented in our hashmap that has keys of asicc list and will append to its value list things that match the key 

this removes the sort and makes it O(n) instead of O(log(n^2))
optimal time : O(n) space : O(n)
'''
from collections import defaultdict
def groupAnagrams(strs):
    myMap = defaultdict(list)
    # O(n)
    for word in strs: 
        # O(1)
        ascii = [0] * 26
        # O(k)
        for letter in word: 
            ascii[((ord(letter) - ord('a')))] += 1

        # O(1)
        myMap[tuple(ascii)].append(word)
    #O(n)
    return list(myMap.values())


            



