'''
RAMPER
R - restate the problem
    given an array of itnegern nums 
    return the top k elmenets that are most seen
A - ask any questions 
    none right now 
M - make an exmpale 
    [2,2,2,2,2,1] k = 2
    [1,2]
P - pick a pattern 
    heap
    frequency hashmap
E - explain the plan
    build a frequency hashmap 
    generate a list of tuples putting the 
    (frequency of eleemnt, values)
    utilize a min heap -> max heap 
    to sort the frequency of lements 
    pop k times the values of our frequency of elment list tuple value
    add value in a list
    return the list
'''
import heapq
def topKFrequent(nums,k):
    myMap = {}
    for _, val in enumerate(nums):
        if val not in myMap:
            myMap[val] = 1
            continue 
        myMap[val] += 1
    freqToVal = []
    for k,v in myMap.items():
        freqToVal.append((-1 * v,k))
    res = []
    heapq.hepaify(freqToVal)

    for _ in range(k):
        val = heapify.heappop(freqToVal[0])
        res.append(val)
    return res 


    

