class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count_num1 = collections.Counter(nums1)
        count_num2 = collections.Counter(nums2)
        
        intersect = dict(count_num1 & count_num2)
        
        for k,v in intersect.items():
            result+= [k]*v
        return result

# Get the common k,v pairs from the dictionary generated from the Counter method for both arrays