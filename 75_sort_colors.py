class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 0
        n = len(nums)
        
        while j<n:
            if nums[j]<1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j]>1:
                n -= 1
                nums[j], nums[n] = nums[n], nums[j]
            else:
                j+=1