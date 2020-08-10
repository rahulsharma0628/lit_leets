class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        totalFruit = 0
        leftPtr = 0
        
        ct = collections.Counter()
        
        for i,x in enumerate(tree):
            ct[x]+=1
            
            while len(ct)>=3:
                ct[tree[leftPtr]]-=1
                if ct[tree[leftPtr]]==0:
                    del ct[tree[leftPtr]]
                leftPtr+=1
            totalFruit = max(totalFruit, i-leftPtr+1)
        
        return totalFruit