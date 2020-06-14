from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        countDict = Counter(arr)
        
        lst = list(countDict.items())
        lst.sort(key=lambda x: x[1])
        print(lst)
        
        for i,x in enumerate(lst):
            k = k - x[1]
            if k<0:
                return len(lst) - i
            elif k==0:
                return len(lst) - i - 1