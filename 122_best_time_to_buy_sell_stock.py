class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(len(prices)-1):
            if(prices[i+1]>prices[i])>0:
                max_profit += prices[i+1]-prices[i]
        return max_profit

#The simplest solution I came up with is to check the consecutive values and if the later one is greater then their difference would be
#the profit and keep adding all such combinations.