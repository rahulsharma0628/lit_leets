class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        num_copy = nums[:]
        num_copy.sort()
        
        # print(num_copy)
        # print(nums)
        
        smallerNumber = []
        for num in nums:
            smallerNumber.append(num_copy.index(num))
            # for i,x in enumerate(num_copy):
            #     if x==num:
            #         smallerNumber.append(i)
            #         break
        return smallerNumber