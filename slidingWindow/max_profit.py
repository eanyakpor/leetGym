'''
RAMPER

R - restate the problem 
   given an array of intergers
   choose a day to buy stock
   and a day to sell 
   ensure there in sequential order as you cannot sell before you buy
   if no profit is possible return 0 
A - ask any questions 
   are there any time constriantaints yes legnth of array is 10^5 so a O(n^2) 
   solution would not work
M - make an example 
   [1,3,4,5]
   buy 1 sell 5 
   profit = 4 
   [0,0,0,0,0]
   buy = sell = 
   profit = 0
   [1]
   buy 1 sell 1
   profit = 0
P - pick a pattern 
   greedy 
   buy then sell immedinatly 
   only store max profit 
E - explain the plan 
   P expalins what the approach will be 
   traverse
   first buy
   then sell if its more than buy
   keep track of the max profit 
   only move buy if we see a value less than previous value else just keep finding for max profit 
   [7,1,5,3,6,4]
    b s
    is b > s yes so move b 
    now start keep track of profit 
    return max profit at the end
   [7,1,5,3,6,4] 
        p
      b 
   mp = 0
'''
def maxProfit(prices):
   buy = 0
   mxProfit = 0

   for price in range(1,len(prices)):
      if prices[buy] > prices[price]:
         print('swap', prices[buy], prices[price])
         buy = price

      print('sell', prices[price])
      print('buy', prices[buy])
      mxProfit = max(mxProfit, (prices[price] - prices[buy]))
      print('profit', mxProfit)
   return mxProfit
   

