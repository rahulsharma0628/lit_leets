class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # print(n)
        # nums[0:0] = nums[-k:]
        # nums = nums[0:n]
        
        # for pos in range(k):
        #     nums[0:0] = [nums.pop()]
        #     # print(nums)

        ## The commented code gives out memory error.
        
        supportArray = [0]*len(nums)        
        for i in range(len(nums)):
            supportArray[(i+k)%len(nums)] = nums[i]        
        nums[:] = supportArray
        
        