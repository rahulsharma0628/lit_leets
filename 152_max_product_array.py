class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_by_far, max_by_far = nums[0], nums[0]
        result = max_by_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, min_by_far*curr, max_by_far*curr)
            min_by_far = min(curr, min_by_far*curr, max_by_far*curr)
            max_by_far = temp_max
            result = max(result, max_by_far)
        return result