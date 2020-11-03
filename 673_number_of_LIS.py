class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        if not nums:
            return 0
        
        length = [1 for _ in range(n)]
        count = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                
                if nums[j]<nums[i]:
                    
                    if length[j]+1 > length[i]:
                        length[i], count[i] = length[j]+1, count[j]
                    elif length[j]+1 == length[i]:
                        count[i]+=count[j]
                        
        max_length = max(length)
        
        return sum(cnt for cnt, l in zip(count, length) if l == max_length)
                        