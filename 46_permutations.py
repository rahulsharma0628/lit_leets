class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        numsLength = len(nums)
        result = []
        permutations = deque()
        permutations.append([])
        
        for curr in nums:
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.popleft()

                for j in range(len(oldPermutation)+1):
                    new = list(oldPermutation)
                    new.insert(j, curr)
                
                    if len(new) == numsLength:
                        result.append(new)
                    else:
                        permutations.append(new)
        return result
        