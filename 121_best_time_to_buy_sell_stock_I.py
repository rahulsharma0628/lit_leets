import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = sys.maxsize
        maxProfit = 0
        
        for i in range(len(prices)):
            if (prices[i]<minPrice):
                minPrice = prices[i]
            elif (prices[i] - minPrice > maxProfit):
                maxProfit = prices[i] - minPrice
        return maxProfit
    
    def maxProfit_alternate(self, prices: List[int]) -> int:
        maxProfit = 0        
        for i in range(len(prices)-1):
            if (prices[i]<prices[i+1]):
                maxProfit = max(max(prices[i+1:]) - prices[i], maxProfit)
        return maxProfit
    