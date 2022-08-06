class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        newPrices = []
        lenn = len(prices)
        
        for i, price in enumerate(prices):
            for j in range(i + 1, lenn):
                price2 = prices[j]
                if price2 <= price:
                    newPrices.append(price - price2)
                    break
                    
            else:
                newPrices.append(price)
                
        return newPrices
            
        