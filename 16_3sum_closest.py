class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        min_diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1
            sums = 0
            while lo<hi:
                sums = nums[i]+nums[lo]+nums[hi]
                if abs(sums-target)<abs(min_diff):
                    min_diff = target - sums
                
                if sums<target:
                    lo+=1
                else:
                    hi-=1
            if min_diff==0:
                break
        return target - min_diff