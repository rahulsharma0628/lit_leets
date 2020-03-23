class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)

# subracting the sum of nums from twice the sum of the set of all the values in the list 