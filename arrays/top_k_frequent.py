# notes - 4/13/26
# sorted by freq make sure to not use k arg name in source code casues conflicts
# heapify sorts by first values when tuple is entered in it 
import heapq

def topKFrequent(nums,k):
   freqMap = {}
   for n in nums:
      if n not in freqMap:
         freqMap[n] = 1
         continue
      freqMap[n] += 1
      
   arr = []

   for key,v in freqMap.items():
      arr.append((-v,key))
   
   ans = []
   heapq.heapify(arr)
   count = k
   while k:
      freq,val = heapq.heappop(arr)
      ans.append(val)
      k -= 1

   print('a',ans)
   return ans 
