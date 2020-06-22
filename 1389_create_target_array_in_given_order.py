class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        target = []
        for i,x in enumerate(index):
            target.insert(x,nums[i])
        return target
        
        # target = []
        # for i,x in enumerate(index):
        #     target[x:x] = [nums[i]]    
        # return target 
    
            