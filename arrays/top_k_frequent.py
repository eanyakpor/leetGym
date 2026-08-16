
'''
RAMPER

R - restate problem in own words
A - ask questions 
M - walk through or make examples, one edge case min 
P - pick pattern 
E - pseudocode solution have interview agree before starting it 
R - review test code, edge cases, talk about time /space complexity and potential optimization 

R 
    given nums and k return the top k most frequent elements in the array 
    awnser can be returned any order 
A/M 
    is a negative number and positive counted as one or difference cause theire polar oppsoites
        basically do we have only positive numbers in our array?
    nums =
    [2,2,2,2,2]
    k = 1
    ans - [2]
    will k always be <= the length of nums 
    what if we have a empty nums but k is 3 then what do we return?
    k i s always in the range of the given nums array 

    [1,1,2,2]
    k = 1
    what gets returened here?
    the awser should be [1] or [2] honestly 
    are there any time/space constriants no 
    but for opitmal get better than 
    O(n(log(n)))
P 
    hashmap to store frequency of elements in list 
    heap as it sorts O(n(log(n))) it stores and pops in O(1) time 

E 
    create frequency hashmap 
    so for 
    [1,1,1,2,2,3]
    1 : 3 
    2 : 2
    3 : 1 
    acutlly map values will be 
    so values will be mapped to (freq,element)
    1 : (3, 1)
    2 : (2 , 2)
    3 : (1, 3)
    creating a heap of the values of the hashmap 
    will then sort by frequency min style 
    when i insert the tuple array and transform it as a heap
    than ill just need to pop the second element k times in a result array
    to get  the awsner 
'''

import heapq
def topKFrequent(nums,k):
    def freqElement():
        myMap = {}
        for n in nums:
            if n not in myMap:
                myMap[n] = [1, n]
                continue 
            myMap[n][0] += 1 
        return myMap

    map = freqElement()
    nums = [[freq*-1,element] for freq,element in map.values()]
    heapq.heapify(nums)
    #print('does turn the first elements to - ?', nums)
    res = []
    while k > 0:
        n = heapq.heappop(nums)
        res.append(n[1])
        k -= 1
    return res





