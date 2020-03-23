import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            
        res_dict = collections.Counter(nums)
        res_dict = {k:v for k,v in sorted(res_dict.items(), key=lambda x: x[1], reverse=True)}
        return list(res_dict.keys())[0] if res_dict[list(res_dict.keys())[0]] > int(len(nums)/2) else None
        

# collection.Counter returns a dictionary with keys as the values in list and the values are their count. 

    def majorityElement_alternate(self, nums: List[int]) -> int:
        res_dict = dict()
        for key in set(nums):
            res_dict[key] = 0
        
        for i in nums:
            res_dict[i] += 1
        
        res_dict = {k:v for k,v in sorted(res_dict.items(), key=lambda x: x[1], reverse=True)}
                
        print(res_dict)
        return list(res_dict.keys())[0]