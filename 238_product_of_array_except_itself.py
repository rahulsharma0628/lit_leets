class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #Method:1 -> Space O(1)    
        n = len(nums)
        result = [0]*n
        result[0] = 1
        
        for i in range(1,n):
            result[i] = result[i-1]*nums[i-1]
        right = 1
        for i in reversed(range(n)):
            result[i] = result[i]*right
            right = right*nums[i]
            
        return result
    
    def productExceptSelfAlternate(self, nums: List[int]) -> List[int]:
    #Method:2 -> Space O(n)
        n = len(nums)
        left = [0]*n
        right = [0]*n
        result = [0]*n
        
        left[0] = 1
        right[n-1] = 1
        
        for i in range(1, n):
            left[i] = left[i-1]*nums[i-1]
            right[n-1-i] = right[n-i]*nums[n-i]
        
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result