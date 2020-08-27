from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        duration = [1,7,30]
        dayset = set(days)
        
        @lru_cache(None)
        def dp(i):
            if i>365:
                return 0
            elif i in dayset:
                return min(dp(i+d)+c for c,d in zip(costs, duration))
            else:
                return dp(i+1)
        
        return dp(1)