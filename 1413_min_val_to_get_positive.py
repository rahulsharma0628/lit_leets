class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        diff = [nums[0]]        
        for x in nums[1:]:
            diff.append(diff[-1]+x)
        print(diff)
        
        if min(diff)>=1:
            return 1
        return 1 - min(diff)