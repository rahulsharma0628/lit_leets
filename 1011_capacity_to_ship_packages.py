class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def isOkay(capacity):
            total = 0
            days = 1
            
            for weight in weights:
                total+=weight
                if total>capacity:
                    total = weight
                    days+=1
                    
                    if days>D:
                        return False
            return True
        
        left, right = max(weights), sum(weights)
        
        while left<right:
            mid = left+(right-left)//2
            
            if isOkay(mid):
                right = mid
            else:
                left = mid+1
        return left