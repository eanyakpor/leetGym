from arrays.top_k_frequent import topKFrequent
if __name__ == "__main__":
   

   #inputs = [((1,1,1,2,2,3), 2)]
   inputs = [([1,1,1,2,2,3],2),([1],1),([1,2,1,2,1,2,3,1,3,2],2)]
   for input in inputs:
      print(f"input array {input}", topKFrequent(input[0],input[-1]))
