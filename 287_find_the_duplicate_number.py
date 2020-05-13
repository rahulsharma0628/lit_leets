class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if (nums[i] - nums[i-1]) == 0:
                return nums[i]
    
    def findDuplicateFloyd(self, nums: List[int]) -> int:
        h = t = nums[0]
        
        while True:
            h = nums[nums[h]]
            t = nums[t]
            if h == t:
                break
        
        t = nums[0]
        while True:
            h = nums[h]
            t = nums[t]
            if h == t:
                return h