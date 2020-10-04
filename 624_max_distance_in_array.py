class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        result = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            result = max(result, max(abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0])))
            min_val = min(arrays[i][0], min_val)
            max_val = max(arrays[i][-1], max_val)
            
        return result