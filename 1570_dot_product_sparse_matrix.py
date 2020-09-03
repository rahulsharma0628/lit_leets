class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = nums
        self.b = [i for i,x in enumerate(nums) if x!=0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        bvec = [i for i,x in enumerate(vec.v) if x!=0]
        # print(vec.b)
        # print(self.b)
        
        toMultiply = list(set(vec.b) & set(self.b)) 
        # print(toMultiply)
        
        if not toMultiply:
            return 0
        
        dotProduct = 0
        for i in toMultiply:
            dotProduct+=(self.v)[i]*(vec.v)[i]
        return dotProduct

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)