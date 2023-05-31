from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = 0, 1
        maxProfit = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
                
            else:
                buy = sell
            sell += 1
            
        return maxProfit
            

#  prices = [7,1,5,3,6,4]
#  prices = [7,6,4,3,1]       
                
            
            