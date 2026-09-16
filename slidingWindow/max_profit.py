'''
UMPIRE
U:
   given a price intenger array
   return the max profit you can have by buying one day and selling another day
   if there are no profits to be made return 0
M: 
   greedy 
   sliding window 
P:
   iterate through the array
   utilize two pointers 
   buy == left
   sell == right
   if buy > sell
   move buy to sell
   so have buy being the maxium number
   keep track of the max profit 
   while we iterate through the array 

'''
def maxProfit(prices):
   maxProfit = 0
   minBuy = 0
   for price in range(len(prices)):
      minBuy = min(minBuy, prices[price])
      maxProfit = max(maxProfit, prices[price] - minBuy):
   return maxProfit



