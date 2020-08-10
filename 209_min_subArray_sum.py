class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums)<s:
            return 0
        
        leftPtr = 0
        sumArr = 0
        minLen = float('inf')
        
        for i in range(len(nums)):
            sumArr+=nums[i]
            
            while sumArr>=s:
                minLen = min(minLen, i-leftPtr+1)
                sumArr-= nums[leftPtr]
                leftPtr+=1
                
        return minLen
                
        
