class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s)/2)):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    
# 1. Swapped the index value with the corresponding index from the right of the list