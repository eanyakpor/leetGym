
def maxProfit(prices):
   buy = 0
   mx = 0
   for sell in range(1,len(prices)):
      if prices[buy] < prices[sell]:
         buy = sell
         continue
      mx = max(mx,(prices[sell] - prices[buy]))
   return mx 
