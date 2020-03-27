import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_d = collections.Counter(nums)
        
        num_d = {k:v for k,v in sorted(num_d.items(), key=lambda x:x[1], reverse=True)}
        return list(num_d.keys())[:k]